from extensions import db
from sqlalchemy.dialects.mysql import INTEGER
import hashlib
import os

class UserJWT(db.Model):
    __tablename__ = 'users_jwt'

    id = db.Column(INTEGER(unsigned=True), primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def __init__(self, email, password):
        self.email = email
        self.set_password(password)

    def set_password(self, password):
        # Parámetros moderados para scrypt que balancean seguridad y consumo de memoria
        n = 2**14   # 16384 (puedes bajar a 2**13 = 8192 si aún hay problemas)
        r = 8
        p = 1
        salt = os.urandom(16)  # Genera un salt aleatorio de 16 bytes
        key = hashlib.scrypt(
            password.encode('utf-8'),
            salt=salt,
            n=n,
            r=r,
            p=p,
            dklen=32
        )
        self.password_hash = f"scrypt:{n}:{r}:{p}${salt.hex()}${key.hex()}"

    def check_password(self, password):
        try:
            # Extraemos los parámetros y datos del hash almacenado
            algo_params, encoded_salt, encoded_key = self.password_hash.split('$')
            _, n_str, r_str, p_str = algo_params.split(':')
            n, r, p = int(n_str), int(r_str), int(p_str)
            salt = bytes.fromhex(encoded_salt)
            key = bytes.fromhex(encoded_key)

            # Hasheamos la contraseña ingresada con los mismos parámetros
            computed_key = hashlib.scrypt(
                password.encode('utf-8'),
                salt=salt,
                n=n,
                r=r,
                p=p,
                dklen=32
            )

            return computed_key == key
        except Exception as e:
            print("Error checking password:", e)
            return False

-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 31-07-2025 a las 01:59:24
-- Versión del servidor: 10.4.25-MariaDB
-- Versión de PHP: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `api_messages_seti`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `messages`
--

CREATE TABLE `messages` (
  `message_id` varchar(36) NOT NULL,
  `session_id` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `timestamp` datetime NOT NULL,
  `sender` varchar(20) NOT NULL,
  `word_count` int(11) DEFAULT NULL,
  `content_length` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `messages`
--

INSERT INTO `messages` (`message_id`, `session_id`, `content`, `timestamp`, `sender`, `word_count`, `content_length`) VALUES
('msg-123410', 'session-abcdef', 'Hola, ¿cómo puedo ayudarte hoy?', '2023-06-15 14:30:00', 'system', 5, 31),
('msg-123411', 'session-abcdef', 'Hola, ¿cómo puedo ayudarte hoy?', '2023-06-15 14:30:00', 'system', 5, 31),
('msg-123413', 'session-abcdef', 'Hola, ¿cómo puedo ayudarte hoy? ***', '2023-06-15 14:30:00', 'system', 6, 35),
('msg-123425', 'session-abcdef', 'Hola, ¿cómo puedo ayudarte hoy? ***', '2023-06-15 14:30:00', 'system', 6, 35),
('msg-123458', 'session-abcdef', 'Hola, ¿cómo puedo ayudarte hoy?', '2023-06-15 14:30:00', 'system', 5, 31),
('msg-715388', 'session-abcdef', 'Hola, ¿cómo puedo ayudarte hoy?', '2025-07-30 18:55:06', 'system', 5, 31),
('msg-962871', 'session-abcdef', 'Hola, ¿cómo puedo ayudarte hoy?', '2025-07-30 18:53:13', 'system', 5, 31);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users_jwt`
--

CREATE TABLE `users_jwt` (
  `id` int(11) NOT NULL,
  `email` varchar(120) NOT NULL,
  `password_hash` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `users_jwt`
--

INSERT INTO `users_jwt` (`id`, `email`, `password_hash`) VALUES
(3, 'camilo@pruebas.com', 'scrypt:16384:8:1$890af8aa0c4a529bad48dedd39d7dc9c$8d0ef341f30835c776528a0e7802bdbc4daf693f29ef45fce0bea284a7d87eab');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`message_id`);

--
-- Indices de la tabla `users_jwt`
--
ALTER TABLE `users_jwt`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `users_jwt`
--
ALTER TABLE `users_jwt`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-03-2020 a las 19:21:07
-- Versión del servidor: 10.4.6-MariaDB
-- Versión de PHP: 7.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `nmap`
--
CREATE DATABASE IF NOT EXISTS `nmap` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `nmap`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `puertos`
--

DROP TABLE IF EXISTS `puertos`;
CREATE TABLE `puertos` (
  `nombre` varchar(30) NOT NULL,
  `status` varchar(30) NOT NULL,
  `service` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `puertos`
--

INSERT INTO `puertos` (`nombre`, `status`, `service`) VALUES
('299/tcp', 'open', 'ftp'),
('8080/tcp', 'close', 'ftp'),
('80/tcp', 'open', 'http'),
('22/tcp', 'open', 'ssh'),
('80/tcp', 'open', 'http');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

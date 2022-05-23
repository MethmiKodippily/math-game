-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 10, 2020 at 03:43 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `python math game`
--

-- --------------------------------------------------------

--
-- Table structure for table `score`
--

CREATE TABLE `score` (
  `name` varchar(100) NOT NULL,
  `correct` int(11) NOT NULL,
  `totalQuestions` int(11) NOT NULL,
  `percentage` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `score`
--

INSERT INTO `score` (`name`, `correct`, `totalQuestions`, `percentage`) VALUES
('dsf', 0, 1, 0),
('b', 1, 3, 33),
('f', 3, 5, 60),
('g', 2, 3, 67),
('Methmi', 5, 5, 100),
('Rajeev', 0, 3, 0),
('methmi', 3, 5, 60),
('methmi', 5, 7, 71),
('methmi', 5, 5, 100),
('Ryan', 0, 2, 0),
('methmi', 3, 5, 60),
('methmi', 5, 7, 71),
('methmi', 4, 5, 80),
('kyfy', 2, 5, 40),
('jed', 2, 5, 40),
('methmi', 1, 3, 33),
('methmi', 4, 5, 80),
('', 2, 5, 40),
('methmi', 4, 5, 80),
('methmi', 4, 7, 57),
('methmi', 3, 5, 60),
('methmi', 7, 7, 100),
('methmi', 4, 5, 80),
('methmi', 3, 3, 100),
('methmi', 5, 5, 100),
('methmi', 4, 5, 80),
('methmi', 2, 3, 67),
('methmi', 3, 3, 100),
('methmi', 3, 4, 75),
('methmi', 3, 5, 60);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

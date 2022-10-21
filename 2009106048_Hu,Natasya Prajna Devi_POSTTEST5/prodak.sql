-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 21, 2022 at 04:16 PM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 7.4.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nutez20`
--

-- --------------------------------------------------------

--
-- Table structure for table `prodak`
--

CREATE TABLE `prodak` (
  `id` int(11) NOT NULL,
  `nomor_produk` int(10) NOT NULL,
  `nama_produk` varchar(40) NOT NULL,
  `jumlah_produk` int(255) NOT NULL,
  `harga_produk` varchar(12) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `prodak`
--

INSERT INTO `prodak` (`id`, `nomor_produk`, `nama_produk`, `jumlah_produk`, `harga_produk`) VALUES
(1, 12121, 'Pensil 2C', 10, '5000'),
(6, 11, 'Sidu 50', 12, '56000'),
(9, 2121, 'Crayon Pensil', 12, '56000'),
(10, 3333, 'Pensil 2C', 12, '40000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `prodak`
--
ALTER TABLE `prodak`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `prodak`
--
ALTER TABLE `prodak`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

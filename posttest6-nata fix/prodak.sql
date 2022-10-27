-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 27, 2022 at 01:54 PM
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
  `harga_produk` varchar(12) NOT NULL,
  `gambar` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `prodak`
--

INSERT INTO `prodak` (`id`, `nomor_produk`, `nama_produk`, `jumlah_produk`, `harga_produk`, `gambar`) VALUES
(1, 12121, 'Pensil 2C', 10, '5000', ''),
(6, 11, 'Sidu 50', 12, '56000', ''),
(9, 2121, 'Crayon Pensil', 12, '56000', ''),
(10, 3333, 'Pensil 2C', 12, '40000', ''),
(14, 11, 'Sidu 42', 100, '56000', ''),
(15, 2121, 'Pensil 2C', 100, '40000', 'data_7_astro-boy-png-33png'),
(16, 2121, 'Sidu 50', 12, '10000', 'image_2022-10-27_115831548png'),
(18, 3333, 'Pensil 2C', 12, '5000', 'CalisTampilphp - posttest5 - Visual Studio Code 10_27_2022 11_56_50 AM'),
(23, 4444, 'Pensil Warna 56', 100, '46000', ''),
(24, 4441, 'Pensil Warna 22', 10, '10000', ''),
(26, 1213, 'Crayon Pensil 20', 10, '56000', 'CalisTampilphp - posttest5 - Visual Studio Code 10_27_2022 11_56_50 AM'),
(33, 3333, 'Penghapus 2B', 100, '56000', ''),
(38, 3333, 'Pensil 2C', 120, '56000', 'data_7_astro-boy-png-33png'),
(41, 2121, 'Crayon Pensil', 100, '40000', ''),
(45, 3333, 'Crayon Pensil', 120, '5000', ''),
(47, 21212, 'Penghapus 2B1', 122, '40000', '');

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
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

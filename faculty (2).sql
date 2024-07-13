-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 22, 2023 at 08:13 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

6


g/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `faculty`
--

-- --------------------------------------------------------

--
-- Table structure for table `achievement`
--

CREATE TABLE `achievement` (
  `achievement_id` varchar(50) NOT NULL,
  `faculty_id` varchar(50) NOT NULL,
  `Date` date NOT NULL,
  `Description` varchar(500) NOT NULL,
  `prof_of_doc` varchar(50) NOT NULL,
  `val_manager_id` varchar(50) NOT NULL,
  `approval_status` varchar(3) DEFAULT 'NO'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `administrator`
--

CREATE TABLE `administrator` (
  `name` varchar(50) NOT NULL,
  `dob` date NOT NULL,
  `email` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `administrator`
--

INSERT INTO `administrator` (`name`, `dob`, `email`) VALUES
('1BI23ADCSE', '2023-01-22', 'adminCSE@gmail.com'),
('xyz', '2022-12-26', 'xyz@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `experience`
--

CREATE TABLE `experience` (
  `faculty_id` varchar(50) NOT NULL,
  `Experience_type` varchar(20) NOT NULL,
  `number_of_years` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `experience`
--

INSERT INTO `experience` (`faculty_id`, `Experience_type`, `number_of_years`) VALUES
('BICSEF01', 'ex', 5);

--
-- Triggers `experience`
--
DELIMITER $$
CREATE TRIGGER `check_exp` BEFORE UPDATE ON `experience` FOR EACH ROW BEGIN  
   
   DECLARE error_msg VARCHAR(255);  
   SET error_msg = ('The Number of years of Experience cannot be less than previous experience');  
    IF new.number_of_years < old.number_of_years THEN  
    SIGNAL SQLSTATE '45000'   
    SET MESSAGE_TEXT = error_msg;  
    END IF;  
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `faculty`
--

CREATE TABLE `faculty` (
  `Fname` varchar(50) NOT NULL,
  `Mname` varchar(50) NOT NULL,
  `Lname` varchar(50) NOT NULL,
  `Email` varchar(30) NOT NULL,
  `faculty_id` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  `department_id` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `faculty`
--

INSERT INTO `faculty` (`Fname`, `Mname`, `Lname`, `Email`, `faculty_id`, `password`, `department_id`) VALUES
('Dr.J.Girija', '', '', 'girija.bitcse@gmail.com', 'BICSEF01', 'faculty1', 'CSE'),
('Manjunath.', 'H', '', 'manjunathh@bit-bangalore.edu.i', 'BICSEF02', 'faculty2', 'CSE'),
('N.Thanuja', '', '', 'thanu.any21@gmail.com', 'BICSEF03', 'faculty3', 'CSE'),
('Vidya', 'R', '', 'vidyar@bit-bangalore.edu.in', 'BICSEF04', 'faculty4', 'CSE'),
('K.N.Prashanth', 'Kumar', '', 'prashanthkumarkn@bit-bangalore', 'BICSEF05', 'faculty5', 'CSE'),
('D.R.Nagamani', '', '', 'drnagamani@bit-bangalore.edu.i', 'BICSEF06', 'faculty6', 'CSE');

-- --------------------------------------------------------

--
-- Table structure for table `qualification`
--

CREATE TABLE `qualification` (
  `Qualification_name` varchar(50) NOT NULL,
  `faculty_id` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `achievement`
--
ALTER TABLE `achievement`
  ADD PRIMARY KEY (`achievement_id`),
  ADD KEY `faculty_id` (`faculty_id`),
  ADD KEY `val_manager_id` (`val_manager_id`);

--
-- Indexes for table `administrator`
--
ALTER TABLE `administrator`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `experience`
--
ALTER TABLE `experience`
  ADD PRIMARY KEY (`faculty_id`) USING BTREE;

--
-- Indexes for table `faculty`
--
ALTER TABLE `faculty`
  ADD PRIMARY KEY (`faculty_id`),
  ADD UNIQUE KEY `fid` (`Email`);

--
-- Indexes for table `qualification`
--
ALTER TABLE `qualification`
  ADD PRIMARY KEY (`Qualification_name`,`faculty_id`),
  ADD KEY `faculty_id` (`faculty_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;

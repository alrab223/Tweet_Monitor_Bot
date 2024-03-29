/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
USE bot;

CREATE TABLE IF NOT EXISTS `flag_control` (
  `flag_name` text DEFAULT NULL,
  `flag` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `flag_control` DISABLE KEYS */;
INSERT INTO `flag_control` (`flag_name`, `flag`) VALUES
	('tweet_get', 0);
/*!40000 ALTER TABLE `flag_control` ENABLE KEYS */;

CREATE TABLE IF NOT EXISTS `Twitter_log` (
  `tweet_id` text DEFAULT NULL,
  `screen_id` text DEFAULT NULL,
  `user` text DEFAULT NULL,
  `text` text DEFAULT NULL,
  `icon` text DEFAULT NULL,
  `media1` text DEFAULT NULL,
  `media2` text DEFAULT NULL,
  `media3` text DEFAULT NULL,
  `media4` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

/*!40000 ALTER TABLE `Twitter_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `Twitter_log` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

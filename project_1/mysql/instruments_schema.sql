-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema Instruments_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `Instruments_schema` ;

-- -----------------------------------------------------
-- Schema Instruments_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Instruments_schema` DEFAULT CHARACTER SET utf8 ;
USE `Instruments_schema` ;

-- -----------------------------------------------------
-- Table `Instruments_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Instruments_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(245) NOT NULL,
  `last_name` VARCHAR(245) NOT NULL,
  `email` VARCHAR(245) NOT NULL,
  `password` VARCHAR(245) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Instruments_schema`.`instruments`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Instruments_schema`.`instruments` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(245) NOT NULL,
  `brand` VARCHAR(245) NOT NULL,
  `type` VARCHAR(245) NOT NULL,
  `price` INT NOT NULL,
  `year` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_instruments_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_instruments_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `Instruments_schema`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

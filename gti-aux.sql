-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema GTI
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `gtidb` ;


-- -----------------------------------------------------
-- Schema GTI
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `gtidb` DEFAULT CHARACTER SET utf8 ;
USE `gtidb` ;


-- -----------------------------------------------------
-- Table `gtidb`.`Colegio`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `gtidb`.`Colegio`;

CREATE TABLE IF NOT EXISTS `gtidb`.`Colegio`(
  `nombre` VARCHAR(255) NOT NULL,
  `hash` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`hash`),
  unique INDEX `hash_unique` (`hash` ASC))
  ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `gtidb`.`TipoPregunta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gtidb`.`TipoPregunta` ;

CREATE TABLE IF NOT EXISTS `gtidb`.`TipoPregunta` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(3) NOT NULL,
  `descripcion` TEXT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `tipo_UNIQUE` (`tipo` ASC)
  
  )
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `gtidb`.`TipoEstructura`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gtidb`.`TipoEstructura` ;

CREATE TABLE IF NOT EXISTS `gtidb`.`TipoEstructura` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tipo` VARCHAR(45) NOT NULL,
  `descripcion` TEXT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `tipo_UNIQUE` (`tipo` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gtidb`.`TipoEdad`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gtidb`.`TipoEdad` ;

CREATE TABLE IF NOT EXISTS `gtidb`.`TipoEdad` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `tipo_edad` VARCHAR(45) NOT NULL,
  `franja_edad` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  UNIQUE INDEX `tipo_edad_UNIQUE` (`tipo_edad` ASC))
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `gtidb`.`Pregunta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gtidb`.`Pregunta` ;

CREATE TABLE IF NOT EXISTS `gtidb`.`Pregunta` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `pregunta` TEXT NOT NULL,
  `tipo_estructura` INT NOT NULL,
  `tipo_pregunta` INT NOT NULL,
  `tipo_edad` INT NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `id_idx` (`tipo_pregunta` ASC),
  INDEX `id_idx1` (`tipo_edad` ASC),
  INDEX `id_idx2` (`tipo_estructura` ASC),
  CONSTRAINT `idTipoPregunta`
    FOREIGN KEY (`tipo_pregunta`)
    REFERENCES `gtidb`.`TipoPregunta` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `idTipoEstructura`
    FOREIGN KEY (`tipo_estructura`)
    REFERENCES `gtidb`.`TipoEstructura` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `idGrupoPregunta`
    FOREIGN KEY (`tipo_edad`)
    REFERENCES `gtidb`.`TipoEdad` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `gtidb`.`Test`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `gtidb`.`Test`;

CREATE TABLE IF NOT EXISTS `gtidb`.`Test`(
`id` INT NOT NULL AUTO_INCREMENT,
`estructura` INT NOT NULL,
`colegio` VARCHAR(255) NOT NULL,
`fecha_cierre` DATETIME NOT NULL,
`school_year` INT NOT NULL,
`first` INT NULL,
`followUp` INT NULL,
`final` INT NULL,
PRIMARY KEY(`id`),
UNIQUE INDEX `id_UNIQUE` (`id` ASC),
INDEX `idEstructura_idx` (`estructura` ASC),
INDEX `idFirst_idx` (`first` ASC),
CONSTRAINT `idEstructuraTest`
    FOREIGN KEY (`estructura`)
    REFERENCES `gtidb`.`TipoEstructura` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
CONSTRAINT `idColegioTest`
    FOREIGN KEY (`colegio`)
    REFERENCES `gtidb`.`Colegio` (`hash`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
    )
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `gtidb`.`PreguntasTest`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gtidb`.`PreguntasTest` ;

CREATE TABLE IF NOT EXISTS `gtidb`.`PreguntasTest` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `test` INT NOT NULL,
  `pregunta` INT NOT NULL,
  `colegio` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `id_idx` (`pregunta` ASC),
  INDEX `idTest_idx` (`test` ASC),
  CONSTRAINT `idPregunta`
    FOREIGN KEY (`pregunta`)
    REFERENCES `gtidb`.`Pregunta` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `idTest`
    FOREIGN KEY (`test`)
    REFERENCES `gtidb`.`Test` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT `idColegioPtest`
    FOREIGN KEY (`colegio`)
    REFERENCES `gtidb`.`Colegio` (`hash`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `gtidb`.`AlumnosTest`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gtidb`.`AlumnosTest`;

CREATE TABLE IF NOT EXISTS `gtidb`.`AlumnosTest`(
  `id` INT NOT NULL AUTO_INCREMENT,
  `test` INT NOT NULL,
  `colegio` VARCHAR(255) NOT NULL,
  `alumno` INT NOT NULL,
  `respuesta` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `idTest_idx` (`test` ASC),
  INDEX `idAlumno_idx` (`alumno` ASC),
  CONSTRAINT `idTestAlumno`
  FOREIGN KEY (`test`) REFERENCES `gtidb`.`Test` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  CONSTRAINT `idAlumnoTest` 
  FOREIGN KEY (`alumno`) REFERENCES `gtidb`.`alumno` (`id`) 
  ON DELETE CASCADE 
  ON UPDATE CASCADE,
  CONSTRAINT `idColegioAtest`
    FOREIGN KEY (`colegio`)
    REFERENCES `gtidb`.`Colegio` (`hash`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
    CONSTRAINT `idRespuesta`
    FOREIGN KEY (`respuesta`)
    REFERENCES `gtidb`.`Respuesta` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `gtidb`.`Alumno`
-- -----------------------------------------------------

DROP TABLE IF EXISTS `gtidb`.`Alumno`;
CREATE TABLE IF NOT EXISTS `gtidb`.`Alumno`(
  `id` INT NOT NULL AUTO_INCREMENT,
  `sexo` VARCHAR(1) NOT NULL,
  `activo` INT NOT NULL DEFAULT 1,
  `nombre` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC)
)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `gtidb`.`Respuesta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `gtidb`.`Respuesta`;
CREATE TABLE IF NOT EXISTS `gtidb`.`Respuesta`(
  `id` INT NOT NULL AUTO_INCREMENT,
  `alumno` INT NOT NULL,
  `pregunta` INT NOT NULL,
  `respuesta` TEXT NULL,
  `colegio` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC),
  INDEX `idAlumno_idx` (`alumno` ASC),
  INDEX `idPregunta_idx` (`pregunta` ASC),
  CONSTRAINT `IdAlumnoRespuesta` FOREIGN KEY (`alumno`)
  REFERENCES `gtidb`.`AlumnosTest` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  CONSTRAINT `idPreguntaRespuesta` FOREIGN KEY (`pregunta`)
  REFERENCES `gtidb`.`Pregunta` (`id`)
  ON DELETE CASCADE
  ON UPDATE CASCADE,
  CONSTRAINT `idColegioRespuesta`
    FOREIGN KEY (`colegio`)
    REFERENCES `gtidb`.`Colegio` (`hash`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
  ENGINE = InnoDB;



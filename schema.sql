CREATE TABLE IF NOT EXISTS `satisfaction_scores` 
(
    `Customer_ID` FLOAT NOT NULL,
    `Engagement_Score` FLOAT DEFAULT NULL,
    `Experience_Score` FLOAT DEFAULT NULL,
    `Satisfaction_Score` FLOAT DEFAULT NULL,
    `Cluster` INT DEFAULT NULL
);

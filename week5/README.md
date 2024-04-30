### Task 2
- CREATE DATABASE website;  
<img width="332" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/b2e3961c-66b8-40ba-887f-0ec31850b641"><br>
- CREATE TABLE member (  
  id BIGINT PRIMARY KEY AUTO_INCREMENT,  
  name VARCHAR(255) NOT NULL,  
  username VARCHAR(255) NOT NULL,  
  password VARCHAR(255) NOT NULL,  
  follower_count INT UNSIGNED NOT NULL DEFAULT 0,  
  time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);  
<img width="524" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/e530f92b-f44b-44ea-9d1d-c3eb3d1eed96"><br>
### Task 3
- INSERT INTO member (name, username, password)  
  VALUES ("test", "test", "test");
  
  INSERT INTO member (name, username, follower_count, password)  
  VALUES ("user1", "username1", 115, "password1");
  
  INSERT INTO member (name, username, follower_count, password)  
  VALUES ("user2", "username2", 35, "password2");
  
  INSERT INTO member (name, username, password)  
  VALUES ("user3", "username3", "password3");
  
  INSERT INTO member (name, username, password)  
  VALUES ("user4", "username4", "password4");  
<img width="635" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/1ec2bc3c-8658-4186-8471-d62d9271d376"><br>
- SELECT * FROM member;  
<img width="711" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/239e63bd-7cc1-4e5f-8e0a-87f1a599fc27"><br>
- SELECT * FROM member ORDER BY time DESC;  
<img width="714" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/5e609ad7-b12a-495e-b18d-dc739812b17c"><br>
- SELECT * FROM member ORDER BY time DESC  
  LIMIT 3 OFFSET 1;  
<img width="710" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/8b4726e0-f275-4ed9-938b-5b451d383d42"><br>
- SELECT * FROM member WHERE name="test";
<img width="679" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/b48001a6-da50-4b24-ab25-a6553bbcbbee"><br>
- SELECT * FROM member WHERE name LIKE "%es%";
<img width="675" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/cc1153ff-b728-4d6c-b1d9-e74279f0ed69"><br>
- SELECT * FROM member WHERE username="test" AND password="test";
<img width="676" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/d7f34b42-41fe-42fb-a384-1a0f1e3280a8"><br>
- UPDATE member SET name="test2" WHERE username="test";
<img width="548" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/856b0ad8-9a2a-4d1e-a994-cca183772164"><br>
### Task 4
- SELECT COUNT(*) FROM member;  
<img width="330" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/26f798c6-6456-4e1c-ac4c-3bb4113f704a"><br>
- SELECT SUM(follower_count) FROM member;  
<img width="424" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/b2537066-f005-4272-9c28-051959160331"><br>
- SELECT AVG(follower_count) FROM member;  
<img width="432" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/4b4a97db-7762-48a8-8834-97f306ec4d7d"><br>
- SELECT AVG(follower_count) FROM member  
  ORDER BY follower_count DESC  
  LIMIT 2;  
  <img width="416" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/dd95173b-f451-4b82-9994-0fd8712ac052"><br>
### Task 5
- CREATE TABLE message (  
  id BIGINT PRIMARY KEY AUTO_INCREMENT,  
  member_id BIGINT NOT NULL,  
  content VARCHAR(255) NOT NULL,  
  like_count INT UNSIGNED NOT NULL DEFAULT 0,  
  time DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,  
  FOREIGN KEY (member_id) REFERENCES member(id));  
<img width="516" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/56948476-28c3-44d2-9a02-4c89cc481329"><br>
- SELECT * FROM message  
  JOIN member ON message.member_id=member.id;
![image](https://github.com/loshuyen/wehelp-stage1/assets/138111003/7725ce17-1ec7-426c-aa61-c0de004fb710)<br>
- SELECT * FROM message  
  JOIN member ON message.member_id=member.id  
  WHERE member.username=“test”;  
<img width="1330" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/f5b8c44a-2e3d-4605-8487-0165a0f0ed1d"><br>
- SELECT member.username, AVG(message.like_count) FROM message  
  JOIN member ON message.member_id=member.id  
  GROUP BY member.username;  
<img width="617" alt="image" src="https://github.com/loshuyen/wehelp-stage1/assets/138111003/a5d684ba-c07b-4093-89b6-65df4048de0d"><br>















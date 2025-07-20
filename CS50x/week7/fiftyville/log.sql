-- ## Who left the bakery day of theft around 10:15am?

-- sqlite> SELECT * FROM bakery_security_logs WHERE month = 7 AND day = 28 AND hour = 10 AND minute > 15 AND minute < 25;

-- ---

-- 260  2024  7      28   10    16      exit      5P2BI95
-- 261  2024  7      28   10    18      exit      94KL13X
-- 262  2024  7      28   10    18      exit      6P58WS2
-- 263  2024  7      28   10    19      exit      4328GD8
-- 264  2024  7      28   10    20      exit      G412CB7
-- 265  2024  7      28   10    21      exit      L93JTIZ
-- 266  2024  7      28   10    23      exit      322W7JE
-- 267  2024  7      28   10    23      exit      0NTHK55

-- ## Who do these license plates belong to?

-- sqlite> SELECT * FROM people
-- ...> WHERE license_plate IN (
-- (x1...>   '5P2BI95',
-- (x1...>   '94KL13X',
-- (x1...>   '6P58WS2',
-- (x1...>   '4328GD8',
-- (x1...>   'G412CB7',
-- (x1...>   'L93JTIZ',
-- (x1...>   '322W7JE',
-- (x1...>   '0NTHK55'
-- (x1...> );
-- id      name     phone_number    passport_number  license_plate

-- ---

-- 221103  Vanessa  (725) 555-4692  2963008352       5P2BI95
-- 243696  Barry    (301) 555-4174  7526138472       6P58WS2
-- 396669  Iman     (829) 555-5269  7049073643       L93JTIZ
-- 398010  Sofia    (130) 555-0289  1695452385       G412CB7
-- 467400  Luca     (389) 555-5198  8496433585       4328GD8
-- 514354  Diana    (770) 555-1861  3592750733       322W7JE
-- 560886  Kelsey   (499) 555-9472  8294398571       0NTHK55
-- 686048  Bruce    (367) 555-5533  5773159633       94KL13X

-- ## Who withdrew money on July 28th?

-- sqlite> SELECT * FROM atm_transactions WHERE month = 7 AND day = 28 and atm_location IS 'Leggett Street' AND transaction_type = 'withdraw';
-- id   account_number  year  month  day  atm_location    transaction_type  amount

-- ---

-- 246  28500762        2024  7      28   Leggett Street  withdraw          48
-- 264  28296815        2024  7      28   Leggett Street  withdraw          20
-- 266  76054385        2024  7      28   Leggett Street  withdraw          60
-- 267  49610011        2024  7      28   Leggett Street  withdraw          50
-- 269  16153065        2024  7      28   Leggett Street  withdraw          80
-- 288  25506511        2024  7      28   Leggett Street  withdraw          20
-- 313  81061156        2024  7      28   Leggett Street  withdraw          30
-- 336  26013199        2024  7      28   Leggett Street  withdraw          35

-- ## Who do these account numbers belong to?

-- sqlite> SELECT account_number, person_id
-- ...> FROM bank_accounts
-- ...> WHERE account_number IN (
-- (x1...>   28500762, 28296815, 76054385, 49610011,
-- (x1...>   16153065, 25506511, 81061156, 26013199
-- (x1...> );
-- account_number  person_id

-- ---

-- 49610011        686048
-- 26013199        514354
-- 16153065        458378
-- 28296815        395717
-- 25506511        396669
-- 28500762        467400
-- 76054385        449774
-- 81061156        438727

-- sqlite> SELECT id, name, phone_number, passport_number, license_plate
-- ...> FROM people
-- ...> WHERE id IN (
-- (x1...>   686048, 514354, 458378, 395717,
-- (x1...>   396669, 467400, 449774, 438727
-- (x1...> );
-- id      name     phone_number    passport_number  license_plate

-- ---

-- 395717  Kenny    (826) 555-1652  9878712108       30G67EN
-- 396669  Iman     (829) 555-5269  7049073643       L93JTIZ
-- 438727  Benista  (338) 555-6650  9586786673       8X428L0
-- 449774  Taylor   (286) 555-6063  1988161715       1106N58
-- 458378  Brooke   (122) 555-4581  4408372428       QX4YZN3
-- 467400  Luca     (389) 555-5198  8496433585       4328GD8
-- 514354  Diana    (770) 555-1861  3592750733       322W7JE
-- 686048  Bruce    (367) 555-5533  5773159633       94KL13X

-- ## Now that we have 2 lists, lets cross-reference and keep duplicates:
-- - **Bruce** (94KL13X)
-- - **Diana** (322W7JE)
-- - **Iman** (L93JTIZ)
-- - **Luca** (4328GD8)

-- ## What was the first flight out of Fiftyville on July 29th?

-- id  origin_airport_id  destination_airport_id  year  month  day  hour  minute

-- ---

-- 36  8                  4                       2024  7      29   8     20

-- ### This is a flight from Fiftyville to LaGuardia!

-- ## Who was on flight 36 to LaGuardia?

-- sqlite> SELECT * FROM passengers WHERE flight_id = 36;
-- flight_id  passport_number  seat

-- ---

-- 36         7214083635       2A
-- 36         1695452385       3B
-- 36         5773159633       4A
-- 36         1540955065       5C
-- 36         8294398571       6C
-- 36         1988161715       6D
-- 36         9878712108       7A
-- 36         8496433585       7B

-- ## Who do these passport numbers belong to?

-- sqlite> SELECT [p.name](http://p.name), p.passport_number, ps.seat
-- ...> FROM passengers ps
-- ...> JOIN people p ON ps.passport_number = p.passport_number
-- ...> WHERE ps.flight_id = 36;
-- name    passport_number  seat

-- ---

-- Doris   7214083635       2A
-- Sofia   1695452385       3B
-- Bruce   5773159633       4A
-- Edward  1540955065       5C
-- Kelsey  8294398571       6C
-- Taylor  1988161715       6D
-- Kenny   9878712108       7A
-- Luca    8496433585       7B

-- ## Now that we have 3 lists, let’s cross reference again:

-- - Bruce
-- - Luca

-- ## Who made phone calls around the time of the theft and lasted less than a minute?

-- sqlite> SELECT * FROM phone_calls WHERE month IS 7 AND day IS 28 AND duration < 60;
-- id   caller          receiver        year  month  day  duration

-- ---

-- 221  (130) 555-0289  (996) 555-8899  2024  7      28   51
-- 224  (499) 555-9472  (892) 555-8872  2024  7      28   36
-- 233  (367) 555-5533  (375) 555-8161  2024  7      28   45
-- 251  (499) 555-9472  (717) 555-1342  2024  7      28   50
-- 254  (286) 555-6063  (676) 555-6554  2024  7      28   43
-- 255  (770) 555-1861  (725) 555-3243  2024  7      28   49
-- 261  (031) 555-6622  (910) 555-3251  2024  7      28   38
-- 279  (826) 555-1652  (066) 555-9701  2024  7      28   55
-- 281  (338) 555-6650  (704) 555-2131  2024  7      28   54

-- sqlite> SELECT name, phone_number
-- ...> FROM people
-- ...> WHERE phone_number IN (
-- (x1...>   '(130) 555-0289',
-- (x1...>   '(499) 555-9472',
-- (x1...>   '(367) 555-5533',
-- (x1...>   '(286) 555-6063',
-- (x1...>   '(770) 555-1861',
-- (x1...>   '(826) 555-1652',
-- (x1...>   '(338) 555-6650'
-- (x1...> );
-- name     phone_number

-- ---

-- Kenny    (826) 555-1652
-- Sofia    (130) 555-0289
-- Benista  (338) 555-6650
-- Taylor   (286) 555-6063
-- Diana    (770) 555-1861
-- Kelsey   (499) 555-9472
-- Bruce    (367) 555-5533

-- ## Now that we have 4 lists, we can cross reference with our lates list:

-- - BRUCE!!!!!!

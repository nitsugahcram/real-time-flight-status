CREATE TABLE test_active_flights (
     id SERIAL PRIMARY KEY,
     flight_date  DATE NOT NULL,
     flight_status  varchar(6) NOT NULL,
     airline_name  varchar(256) DEFAULT NULL,
     flight_number  varchar(256) DEFAULT NULL,
     departure_airport  varchar(256) DEFAULT NULL,
     departure_timezone  varchar(256) DEFAULT NULL,
     arrival_airport  varchar(256) DEFAULT NULL,
     arrival_timezone  varchar(256) DEFAULT NULL,
     arrival_terminal  varchar(256) DEFAULT NULL,
     insert_timestamp  TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO test_active_flights VALUES("2021-01-25","active","Tibet Airlines","6961","Hangzhou","Asia/Shanghai","Guiyang","Asia/Shanghai","T2");
INSERT INTO test_active_flights VALUES("2021-01-25","active","Air China LTD","5757","Kunming","Asia/Shanghai","Baoshan","Asia/Shanghai","T3");
INSERT INTO test_active_flights VALUES("2021-01-25","active","Kunming Airlines","8333","Kunming","Asia/Shanghai","Baoshan","Asia/Shanghai","T3");
INSERT INTO test_active_flights VALUES("2021-01-25","active","Air Caledonie","307","Magenta","Pacific/Noumea","Ouvea","Pacific/Noumea","");
INSERT INTO test_active_flights VALUES("2021-01-25","active","Okay Airways","6533","Kunming","Asia/Shanghai","Taizhou","Asia/Shanghai","T2");
INSERT INTO test_active_flights VALUES("2021-01-25","active","Xiamen Airlines","5325","Hangzhou","Asia/Shanghai","Guiyang","Asia/Shanghai","T2");
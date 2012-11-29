# -*- coding: latin-1 -*-

#\x84\x94\x81 = äöü	\x8e\x99\x9a = ÄÖÜ


from BaseOps import *

nfemale = ['Adela', 'Adelaide', 'Adele', 'Adelheide', 'Adelina', 'Adeline', 'Adriana', 'Adrienne', 'Afra', 'Agatha', 'Agathe', 'Agda', 'Agnesa', 'Agnesa', 'Agnese', 'Agneta', 'Agnete', 'Agnita', 'Ainoa', 'Alamea', 'Alberta', 'Albertina', 'Albertine', 'Albina', 'Albine', 'Alea', 'Alesja', 'Alessandra', 'Alessia', 'Alesya', 'Aletta', 'Alette', 'Alexandra', 'Alexandrina', 'Alexandrine', 'Alice', 'Alicia', 'Alida', 'Alina', 'Aline', 'Aliyaha', 'Amabele', 'Amanda', 'Amina', 'Ana', 'Anahe', 'Anahi', 'Anahi', 'Anahita', 'Anastasia', 'Andra', 'Andrea', 'Angela', 'Angelina', 'Ania', 'Anine', 'Anita', 'Anja', 'Anke', 'Anna', 'Anna', 'Anndea', 'Anne', 'Anneke', 'Annetta', 'Annette', 'Anni', 'Antje', 'Apollonia', 'Apolonia', 'Aranka', 'Arda', 'Aretha', 'Ariadna', 'Ariadne', 'Ariana', 'Ariana', 'Ariane', 'Ariane', 'Arianna', 'Arife', 'Asta', 'Astride', 'Atalja', 'Audreya', 'Aurelia', 'Aurelie', 'Avdotya', 'Babette', 'Babsi', 'Barbara', 'Barbra', 'Bea', 'Beata', 'Beate', 'Beatrice', 'Beatrixa', 'Beckya', 'Belana', 'Belanna', 'Belinda', 'Beniese', 'Beppina', 'Berta', 'Berte', 'Bertha', 'Berthe', 'Bertina', 'Bertine', 'Betsya', 'Bettina', 'Bettya', 'Binia', 'Birgide', 'Birgita', 'Birgitta', 'Bithiaha', 'Bithja', 'Bitja', 'Blanca', 'Blanche', 'Blanka', 'Bliktrude', 'Brettina', 'Bridgete', 'Brigide', 'Brigitta', 'Brigitte', 'Camilla', 'Camille', 'Cara', 'Cari', 'Carina', 'Carina', 'Carine', 'Carla', 'Carlota', 'Carlotta', 'Carmela', 'Carmelia', 'Carmene', 'Carmina', 'Carola', 'Carola', 'Carole', 'Carolina', 'Carolina', 'Caroline', 'Carolyne', 'Cassandra', 'Caterina', 'Catherine', 'Cathya', 'Caye', 'Ceara', 'Cecilia', 'Cecilie', 'Cecilye', 'Celina', 'Celine', 'Cera', 'Chantala', 'Charlotta', 'Charlotta', 'Charlotte', 'Chiara', 'Chioma', 'Chloe', 'Christa', 'Christela', 'Christiana', 'Christiane', 'Christina', 'Christine', 'Cindye', 'Cinta', 'Cinzia', 'Claire', 'Clara', 'Clare', 'Clarice', 'Clarina', 'Clarina', 'Clarinda', 'Clarinde', 'Clarissa', 'Claude', 'Claudette', 'Claudia', 'Claudina', 'Claudine', 'Coelestina', 'Colomba','Colombe', 'Constance', 'Constanza', 'Constanze', 'Cora', 'Cordula', 'Corina', 'Corinna', 'Corinne', 'Cornela', 'Cornelia', 'Corona', 'Cristina', 'Cunegunda', 'Cunegundesa', 'Cynthia', 'Cyra', 'Dagmare', 'Dairine', 'Dalisaya', 'Damiana', 'Dana', 'Daniela', 'Daniele', 'Daniella', 'Danielle', 'Danila', 'Daria', 'Darina', 'Darina', 'Darja', 'Davida', 'Davina', 'Dea', 'Debbie', 'Debbya', 'Debora', 'Deborahe', 'Deborina', 'Debra', 'Deina', 'Denise', 'Diana', 'Diane', 'Dianne', 'Dollye', 'Domenica', 'Dominica', 'Dominika', 'Dominique', 'Donata', 'Dora', 'Dora', 'Doreene', 'Dorisa', 'Dorotea', 'Dorothea', 'Dorothee', 'Dorothye', 'Dunja', 'Dynella', 'Dynelle', 'Edeltraude', 'Edeltraute', 'Edeltruda', 'Edithe', 'Editha', 'Edoarda', 'Eduarda', 'Edvige', 'Edwige', 'Ehrentraude', 'Ehrentrude', 'Elana', 'Eleanore', 'Elena', 'Eleonora', 'Elisa', 'Elisabetha', 'Elisabetta', 'Elischeba', 'Elise', 'Elizabethe', 'Elke', 'Ellena', 'Ellya', 'Elsa', 'Eltje', 'Elvira', 'Elvire', 'Emanuela', 'Emanuelle', 'Emilia', 'Emilie', 'Emilye', 'Emma', 'Emmanuelle', 'Emmeline', 'Engele', 'Enola', 'Enya', 'Ercelina', 'Ercilia', 'Erdmute', 'Erentraude', 'Erentrude', 'Ermengarda', 'Erna', 'Ernesta', 'Ernestina', 'Ernestine', 'Ersilia', 'Estelle', 'Estrella', 'Eva', 'Evdokia', 'Eve', 'Eveline', 'Evita', 'Fabiana', 'Fabiane', 'Fabienne', 'Fannya', 'Farena', 'Farrena', 'Fausta', 'Faustina', 'Fe', 'Felicia', 'Felicitase', 'Felicitya', 'Felisa', 'Felizia', 'Felizitasa', 'Fenja', 'Fenja', 'Feodora', 'Fina', 'Fiona', 'Flavia', 'Francesa', 'Francesca', 'Francisca', 'Franzi', 'Franziska', 'Gabi', 'Gabriela', 'Gabriele', 'Gabriella', 'Gabrielle', 'Gabya', 'Gaile', 'Gefiona', 'Gela', 'Georgette', 'Georgia', 'Georgina', 'Georgine', 'Geralde', 'Geraldine', 'Gertrude', 'Gertrude', 'Gesa', 'Gese', 'Gesina', 'Gesine', 'Getraude', 'Gianna', 'Gille', 'Gilliana', 'Gina', 'Ginevra', 'Gioana', 'Giovanna', 'Gisela', 'Gisella', 'Giselle', 'Gitta', 'Giulia', 'Giuliana', 'Giulietta', 'Giuseppa', 'Giuseppina', 'Giustina', 'Gladisa', 'Gladysa', 'Gloria', 'Gloriana', 'Grazyna', 'Gretela', 'Griselda', 'Guda', 'Gudrune', 'Gunda', 'Gunde', 'Gundela', 'Gundula', 'Gunloda', 'Gunnloda', 'Gutta', 'Gwena', 'Gwenda', 'Gwendoline', 'Gwendolyne', 'Hadassaha', 'Haidee', 'Haneefa', 'Hanifa', 'Hanifahe', 'Hanife', 'Hanna', 'Hanna', 'Hannaha', 'Hansine', 'Hatice', 'Hatifa', 'Haydee', 'Hazela', 'Hedi', 'Hedviga', 'Hedwiga', 'Hedya', 'Heide', 'Heidi', 'Heilke', 'Helena', 'Helena', 'Helene', 'Helga', 'Helke', 'Hella', 'Helma', 'Henna', 'Henrietta', 'Henriette', 'Herdise', 'Hettye', 'Hiddekela', 'Hidekele', 'Hilaria', 'Hilarya', 'Hilda', 'Hilde', 'Hildegarde', 'Honeye', 'Honorata', 'Ida', 'Ilana', 'Ilaria', 'Ileana', 'Ilenia', 'Ilia', 'Ilka', 'Ilke', 'Ilona', 'Ilse', 'Imka', 'Imke', 'Immacolata', 'Ina', 'Indigoe', 'Inese', 'Inga', 'Inge', 'Ingeborga', 'Ingrida', 'Inola', 'Insa', 'Inse', 'Ioanna', 'Iphigenia', 'Iphigenie', 'Ira', 'Irene', 'Irina', 'Irisa', 'Irma', 'Irmgarda', 'Isabela', 'Isabella', 'Isabelle', 'Isha', 'Iva', 'Ivana', 'Ivona', 'Ivonne', 'Iwana', 'Jackie', 'Jackye', 'Jacqueline', 'Jadwiga', 'Jaele', 'Jaelle', 'Jana', 'Jane', 'Janete', 'Janina', 'Janine', 'Janka', 'Janna', 'Jantje', 'Jarina', 'Jasmina', 'Jasmina', 'Jasmine', 'Jasminka', 'Jasna', 'Jayne', 'Jeanette', 'Jeanne', 'Jeannine', 'Jekaterina', 'Jelena', 'Jelscha', 'Jelsha', 'Jelyssa', 'Jemima', 'Jennifera', 'Jennina', 'Jennye', 'Jennye', 'Jessamyne', 'Jessica', 'Jessie', 'Jessika', 'Jessye', 'Jille', 'Joana', 'Joana', 'Joanna', 'Jocelyne', 'Joelle', 'Johanna', 'Jolie', 'Jona', 'Jonna', 'Josefa', 'Josefina', 'Josefine', 'Joseline', 'Josepha', 'Josiane', 'Juana', 'Juanita', 'Juditha', 'Judye', 'Julia', 'Juliana', 'Juliane', 'Julica', 'Julie', 'Julienne', 'Juliette', 'Julika', 'Justa', 'Justina', 'Justine', 'Kai', 'Kaje', 'Kamilla', 'Kara', 'Karene', 'Karine','Karina', 'Karina', 'Karine', 'Karine', 'Karla', 'Karola', 'Karolina', 'Karoline', 'Kassandra', 'Katarina', 'Kate', 'Katharina', 'Katharine', 'Katherina', 'Katherine', 'Kathleene', 'Kathrina', 'Katia', 'Katina', 'Katinka', 'Katja', 'Katrina', 'Katya', 'Kaye', 'Keanna', 'Kerrina', 'Kerstine', 'Kezia', 'Khadija', 'Kiana', 'Kianna', 'Kima', 'Kimberleya', 'Kimberlya', 'Kinga', 'Kira', 'Klara', 'Klarina', 'Klarinda', 'Klarinde', 'Klarine', 'Klarissa', 'Klaudia', 'Klothilde', 'Klotilda', 'Kolumba', 'Konstantina', 'Konstantine', 'Konstanze', 'Kora', 'Korinna', 'Korinne', 'Kornelia', 'Korona', 'Kristine', 'Kristina', 'Kunegunda', 'Kunigonde', 'Kunigunda', 'Kunigunde', 'Kuniza', 'Kyra', 'Ladina', 'Laila', 'Lara', 'Larina', 'Larisa', 'Larissa', 'Latifa', 'Laura', 'Laure', 'Laureena', 'Laurence', 'Lauretta', 'Layla', 'Lea', 'Leahe', 'Leandra', 'Lee', 'Leia', 'Leigha', 'Leila', 'Leilaha', 'Lena', 'Lena', 'Lene', 'Lenka', 'Lenka', 'Leoni', 'Leonie', 'Leonique', 'Leya', 'Lia', 'Libbya', 'Lidia', 'Liese', 'Liesele', 'Lina', 'Linda', 'Linde', 'Lisa', 'Lisbetha', 'Lise', 'Lisette', 'Liva', 'Livia', 'Lize', 'Liza', 'Lizzie', 'Lora', 'Lorena', 'Lorenza', 'Loretta', 'Lorna', 'Lotte', 'Louisanne', 'Louise', 'Luana', 'Lucia', 'Lucie', 'Ludmilla', 'Luisa', 'Luise', 'Lydia', 'Lydie', 'Mabele', 'Mabra', 'Maddalena', 'Madelane', 'Madeleine', 'Madelena', 'Madeline', 'Madlena', 'Madlena', 'Madlene', 'Magdalene', 'Magdalena', 'Magdalene', 'Maggie', 'Maggya', 'Maia', 'Maike', 'Maira', 'Maja', 'Malaaka', 'Malaka', 'Malika', 'Malvina', 'Malwina', 'Malwine', 'Manavi', 'Mandana', 'Manja', 'Manona', 'Manuela', 'Mara', 'Marcella', 'Marcelle', 'Mareile', 'Marena', 'Maresa', 'Margareta', 'Margareta', 'Margarete', 'Margaretha', 'Margarethe', 'Margarita', 'Margherita', 'Margita', 'Margitta', 'Margote', 'Margreta', 'Margrete', 'Marguerite', 'Maria', 'Mariana', 'Mariane', 'Marianka', 'Marianna', 'Marianne', 'Marie', 'Mariella', 'Marietta', 'Mariette', 'Marija', 'Marika', 'Marina', 'Marine', 'Mariona', 'Mariona', 'Marisa', 'Marisa', 'Mariska', 'Marita', 'Marja', 'Marjorie', 'Marlene', 'Marta', 'Martha', 'Marthe', 'Martina', 'Martine', 'Maruschka', 'Marya', 'Marzanna', 'Marzena', 'Mathilda', 'Mathilde', 'Matilde', 'Maude', 'Maude', 'Maureena', 'Maxima', 'Maye', 'Mechthilda', 'Meeri', 'Mege', 'Melanie', 'Melika', 'Melina', 'Meline', 'Melissa', 'Melitta', 'Mercede', 'Mercedese', 'Merlinda', 'Merlinde', 'Micaela', 'Michaela', 'Michale', 'Micheline', 'Michelle', 'Miguela', 'Mikaela', 'Mila', 'Milena', 'Mireille', 'Mirella', 'Mirjame', 'Mirna', 'Moana', 'Moni', 'Monica', 'Monika', 'Monique', 'Morgana', 'Morgane', 'Myrene', 'Myrine', 'Naara', 'Naarahe', 'Nadeschda', 'Nadezda', 'Nadezhda', 'Nadia', 'Nadine', 'Nadja', 'Nadjana', 'Nadjeschda', 'Naiara', 'Nala', 'Nalani', 'Nancya', 'Nane', 'Nanette', 'Nanna', 'Nannie', 'Naomi', 'Natalia', 'Natalie', 'Natalija', 'Natascha', 'Nathalie', 'Navina', 'Nayara', 'Nayeli', 'Neva', 'Nicola', 'Nicole', 'Nicoletta', 'Nicolette', 'Nikola', 'Nima', 'Nina', 'Noahe', 'Noemi', 'Nora', 'Norma', 'Numa', 'Nurana', 'Nyima', 'Oda', 'Olga', 'Oliva', 'Olive', 'Oliveta', 'Olivia', 'Ornella', 'Orsola', 'Ostara', 'Pame', 'Pamela', 'Paola', 'Paolina', 'Pate', 'Patricia', 'Patrizia', 'Pattya', 'Paula', 'Paule', 'Paulette', 'Pauline', 'Pavla', 'Pepita', 'Petra', 'Pia', 'Piera', 'Pina', 'Praxedisa', 'Prisca', 'Priscilla', 'Priscille', 'Priska', 'Rachele', 'Rachele', 'Rachelle', 'Raeanne', 'Raeanne', 'Rahele', 'Rahsane', 'Ramona', 'Ranae', 'Raquela', 'Rebecca', 'Rebekka', 'Reeme', 'Regina', 'Regula', 'Renata', 'Renate', 'Renee', 'Retha', 'Rhiana', 'Rhianna', 'Riccarda', 'Rihanna', 'Rima', 'Rita', 'Rojane', 'Romea', 'Romilda', 'Rosa', 'Rosalia', 'Rosalie', 'Rosalinda', 'Rosalinde', 'Rose', 'Roseline', 'Rosetta', 'Rosette', 'Rosi', 'Rosina', 'Rosine', 'Rossana', 'Roswita', 'Roswitha', 'Roxana', 'Roxane', 'Roxanne', 'Roxya', 'Rozhane', 'Rukiye', 'Runa', 'Ruqayyahe', 'Ruthe', 'Ryme', 'Sabina', 'Sabine', 'Sabrina', 'Sallya', 'Salome', 'Samanta', 'Samantha', 'Samira', 'Sandra', 'Sandrine', 'Sanne', 'Sanora', 'Sanura', 'Sara', 'Sarahe', 'Sarina', 'Sarine', 'Saskia', 'Sassa', 'Scarlete', 'Scarlette', 'Schwanhilde', 'Selda', 'Seleina', 'Selene', 'Selina', 'Selma', 'Senja', 'Serafina', 'Seraina', 'Seraphina', 'Seraphine', 'Sereina', 'Serena', 'Sevala', 'Severina', 'Sevila', 'Shalimara', 'Sharee', 'Shari', 'Sharona', 'Sheena', 'Sheila', 'Sherina', 'Shila', 'Shirine', 'Shirleya', 'Sibilla', 'Sibyle', 'Sibylla', 'Sibylle', 'Sidonia', 'Sidonie', 'Sigride', 'Sigrieda', 'Sile', 'Silka', 'Silke', 'Silva', 'Silvana', 'Silvia', 'Silviana', 'Simina', 'Simona', 'Simone', 'Simonetta', 'Simonette', 'Sina', 'Siri', 'Snezana', 'Snjezana', 'Sofia', 'Sofie', 'Solidea', 'Solveige', 'Sonia', 'Sonja', 'Sonya', 'Sophia', 'Sophie', 'Stana', 'Stanislava', 'Stanislawa', 'Stefania', 'Stefanie', 'Steffi', 'Stella', 'Stephanie', 'Stina', 'Stine', 'Stintje', 'Sue', 'Sunna', 'Susana', 'Susanna', 'Susanne', 'Susetta', 'Susi', 'Suzanne', 'Suzette', 'Svala', 'Svana', 'Svanhildure', 'Svea', 'Svenja', 'Sybile', 'Sybilla', 'Sybille', 'Sylvia', 'Sylvie', 'Tabea', 'Tabitha', 'Tamaja', 'Tamara', 'Tamika','Tamira', 'Tania', 'Tanita', 'Tanitha', 'Tanja', 'Tanya', 'Tatiana', 'Tatjana', 'Taya', 'Tecla', 'Teodora', 'Teresa', 'Terrye', 'Tesse', 'Tessa', 'Tessie', 'Thea', 'Thekla', 'Theodora', 'Theodore', 'Therese', 'Theresa', 'Therese', 'Theresia', 'Thorhilda','Tina', 'Tine', 'Tineke', 'Tomma', 'Torhilda', 'Torille', 'Tracye', 'Trixi', 'Ulla', 'Ulli', 'Ulrica', 'Ulrika', 'Ulrike', 'Ulrique', 'Unne', 'Ursela', 'Ursina', 'Ursola', 'Ursula', 'Ursule', 'Ursulina', 'Uschi', 'Uta', 'Ute', 'Utta', 'Valena', 'Valentina', 'Valentine', 'Valeria', 'Valerie', 'Valeska', 'Vanda', 'Vanessa', 'Vera', 'Verena', 'Verna', 'Vernetta', 'Veronica', 'Veronika', 'Vickya', 'Victoire', 'Victoria', 'Viktoria', 'Vina', 'Viola', 'Violete', 'Violetta', 'Violette', 'Virginia', 'Virginie', 'Vittoria', 'Viviane', 'Viviana', 'Viviane', 'Viviena', 'Vivienne', 'Vivienne', 'Vreneli', 'Vreni', 'Vroni', 'Waltraude', 'Waltraute', 'Wanda', 'Xenia', 'Yamawadee', 'Yasmine', 'Yekaterina', 'Yela', 'Yuna', 'Yvette', 'Yvonne', 'Zarahe', 'Zelda', 'Zenia', 'Zeruiahe', 'Zeruja', 'Zeruya', 'Zita', 'Zoa', 'Zoe']
nmale = ['Aaron', 'Abel', 'Abraham', 'Achim', 'Adalbero', 'Adam', 'Adamo', 'Adelbert', 'Adolf', 'Adolfo', 'Adolph', 'Adriaan', 'Adriaen', 'Adrian', 'Adriano', 'Adrien', 'Akim', 'Alain', 'Alan', 'Albain', 'Alban', 'Albano', 'Albero', 'Albert', 'Alberto', 'Albin', 'Albrecht', 'Alec', 'Alejandro', 'Aleksandar', 'Aleksandr', 'Alessandro', 'Alessio', 'Alex', 'Alexander', 'Alexandros', 'Alexej', 'Alexis', 'Alexius', 'Alfons', 'Alfonso', 'Alfred', 'Allan', 'Allen', 'Alois', 'Aloisius', 'Alonzo', 'Aloys', 'Aloysius', 'Alphons', 'Alvise', 'Amadeo', 'Amadeus', 'Amando', 'Ambrose', 'Amedeo', 'Amin', 'Anakin', 'Anastasius', 'Anders', 'Andreas', 'Andrej', 'Andres', 'Andrew', 'Andrin', 'Andy', 'Angel', 'Angelo', 'Angelus', 'Ansgar', 'Anthony', 'Anton', 'Antonio', 'Apollo', 'Apollonius', 'Araldo', 'Aram', 'Aramis', 'Archibald', 'Ariano', 'Armand', 'Armando', 'Armin', 'Arnaldo', 'Arnaud', 'Arnault', 'Arnd', 'Arndt', 'Arno', 'Arnold', 'Arnoldo', 'Arnolt', 'Arnoud', 'Aron', 'Arrigo', 'Art', 'Arthur', 'Artur', 'Arturo', 'Arved', 'Arvid', 'Arwed', 'Arwid', 'Asher', 'Asser', 'August', 'Augustin', 'Augustinus', 'Augusto', 'Aurel', 'Austin', 'Axel', 'Baker', 'Baptist', 'Barney', 'Bastian', 'Bastien', 'Beat', 'Beath', 'Beato', 'Ben', 'Benedetto', 'Benedict', 'Benedikt', 'Beniamino', 'Benito', 'Benjamin', 'Benjy', 'Bennett', 'Benno', 'Benny', 'Bernard', 'Bernardo', 'Bernd', 'Berndt', 'Bernhard', 'Bert', 'Berthold', 'Berto', 'Bertoldo', 'Bertram', 'Billy', 'Birk', 'Blase', 'Bob', 'Bobby', 'Borchard', 'Boris', 'Borislav', 'Borislaw', 'Brian', 'Bringfried', 'Bruno', 'Bryan', 'Burghard', 'Burkard', 'Burkart', 'Burkhard', 'Caetano', 'Camill', 'Camillo', 'Camilo', 'Caoimhin', 'Carey', 'Carl', 'Carlo', 'Carlos', 'Carsten', 'Cary', 'Casimir', 'Caspar', 'Cay', 'Cedric', 'Cedrik', 'Celio', 'Charles', 'Chris', 'Christian', 'Christof', 'Christoph', 'Christopher', 'Cillian', 'Claas', 'Claudio', 'Claudius', 'Claus', 'Clemens', 'Coelestin', 'Colin', 'Conan', 'Conrad', 'Conradin', 'Conrado', 'Conradus', 'Constantin', 'Cornel', 'Cornelio', 'Cornelis', 'Cornelius', 'Corrado', 'Cosmin', 'Cosmo', 'Costantino', 'Crispin', 'Cristian', 'Cristiano', 'Cristoforo', 'Curd', 'Curt', 'Curt', 'Curtis', 'Curtiz', 'Curzio', 'Cyril', 'Cyrill', 'Cyrillus', 'Cyrus', 'Daan', 'Damian', 'Damiano', 'Damien', 'Dan', 'Dan', 'Daniel','Danilo', 'Dankmar', 'Danny', 'Dario', 'Darius', 'David', 'Delfred', 'Dempsey', 'Denis', 'Dennis', 'Denny', 'Derek', 'Derk', 'Derrick', 'Detlef', 'Detlev', 'Diarmaid', 'Diarmid', 'Diarmuid', 'Dick', 'Diebald', 'Diego', 'Dieter', 'Dietmar', 'Dietreich', 'Dietrich', 'Dimitrij', 'Dirk', 'Ditmar', 'Dittmar', 'Dolf', 'Domenic', 'Domenico', 'Domingo', 'Dominic', 'Dominik', 'Duarte', 'Duncan', 'Dunstan', 'Dylan', 'Earnest', 'Eberhard', 'Eberhart', 'Eckard', 'Eckhard', 'Ed', 'Eddy', 'Edgar', 'Edgaro', 'Edmond', 'Edmondo', 'Edmund', 'Edoardo', 'Edouard', 'Eduard', 'Eduardo', 'Edvard', 'Edward', 'Edwin', 'Edzard', 'Eggert', 'Egmond', 'Egmont', 'Egmund', 'Egon', 'Ehrenfried', 'Ekkehard', 'Elan', 'Elbasan', 'Elias', 'Elijah', 'Ellmar', 'Elmar', 'Elmer', 'Elric', 'Emanuel', 'Emil', 'Emilio', 'Emmanuel', 'Endrik', 'Enrico', 'Enzio', 'Eric', 'Erich', 'Erik', 'Erkenbald', 'Ermanno', 'Erminio', 'Ernest', 'Ernestin', 'Ernesto', 'Ernst', 'Erwin', 'Eugen', 'Eugenio', 'Fabian', 'Fabiano', 'Fabien', 'Fabio', 'Fabius', 'Fabrizio','Fabrizius', 'Falco', 'Falk', 'Falko', 'Faustus', 'Federico', 'Federigo', 'Fedor', 'Fekry', 'Feliciano', 'Felix', 'Feodor', 'Ferdinand', 'Ferdinando', 'Fernand', 'Fernando', 'Filippo', 'Finn', 'Fionn', 'Fjodor', 'Flavien', 'Flavio', 'Florens', 'Florent', 'Florian', 'Florin', 'Floris', 'Floyd', 'Flurin', 'Francesco', 'Francis', 'Francisco', 'Franciscus', 'Franco', 'Frank', 'Franklin', 'Franko', 'Franz', 'Franziskus', 'Fred', 'Freddy', 'Frederic', 'Frederico', 'Fridjof', 'Fridolin', 'Fridtjof', 'Friedemann','Frieder', 'Friederich', 'Friedrich', 'Fritz', 'Gabriel', 'Gabriello', 'Gaetano', 'Garet', 'Garnier', 'Garrett', 'Gaspar', 'Gaspard', 'Gasparo', 'Gaston', 'Gauthier', 'Gautier', 'Gene', 'Geoffrey', 'Geoffroy', 'Georg', 'Georges', 'Georgius', 'Gerald', 'Geraldo', 'Gerd', 'Gerhard', 'Gerhart', 'Gerhold', 'Germain', 'German', 'Germano', 'Gernot', 'Gero', 'Gerold', 'Geronimo', 'Gerry', 'Gert', 'Giacomo', 'Gian', 'Gianni', 'Gideon', 'Gilbert', 'Gilberto', 'Gilles', 'Gioacchino', 'Giordano', 'Giorgio', 'Giosch','Giraldo', 'Giuliano', 'Giulio', 'Giusto', 'Glen', 'Glenn', 'Godfrey', 'Gordon', 'Gottfried', 'Gregor', 'Gregorio', 'Gregory', 'Gualtiero', 'Guglielmo', 'Guido', 'Guillermo', 'Gundhard', 'Gunter', 'Gunthard', 'Gunther', 'Gus', 'Gustaaf', 'Gustaf', 'Gustav', 'Gustavo', 'Gustl', 'Guy', 'Hadrian', 'Hagen', 'Haithem', 'Hajo', 'Hanif', 'Hannes', 'Hans', 'Hansrudolf', 'Harald', 'Hares', 'Harold', 'Hartmut', 'Hartwig', 'Harvey', 'Haytham', 'Heiko', 'Heiner', 'Heino', 'Heinrich', 'Heinz', 'Hellmuth', 'Helmer', 'Helmut', 'Helmuth', 'Hendrick', 'Hendrik', 'Hennes', 'Henning', 'Henrick', 'Henry', 'Herbert', 'Hercli', 'Herman', 'Hermann', 'Hertwig', 'Hieronymus', 'Hilarius', 'Hillert', 'Hjalmar', 'Holger', 'Horatio', 'Horaz', 'Horst', 'Hubert', 'Hugh', 'Hugo', 'Hugues', 'Humbert', 'Humphrey', 'Hunfried', 'Ibrahim', 'Ignaz', 'Ignazio', 'Igor', 'Ilan', 'Ilay', 'Imko', 'Immanuel', 'Indigo', 'Ingo', 'Ingvar', 'Ioannis', 'Irvin', 'Isaac', 'Isaak', 'Ivan', 'Ivo', 'Iwan', 'Jack', 'Jacky', 'Jacob', 'Jacques', 'Jaeger', 'Jago', 'Jaime', 'Jakob', 'James', 'Jan', 'Janik', 'Janiv', 'Jankin', 'Jarmo', 'Jarno', 'Jason', 'Jasper', 'Javier', 'Jean', 'Jeffrey', 'Jendrik', 'Jens', 'Jeremiah', 'Jeremias', 'Jeremy', 'Jeronimo', 'Jerry', 'Jerry', 'Jesper', 'Jim', 'Jimmy', 'Jo', 'Jo', 'Joachim', 'Joah', 'Jochen', 'Joel', 'Johann', 'Johannes', 'John', 'Johnny', 'Jonah', 'Jonas', 'Jonathan', 'Jonathas', 'Jordan', 'Jordano', 'Joscha', 'Joschua', 'Josef', 'Joseph', 'Josselin', 'Jourdain', 'Juan', 'Juanito', 'Jules', 'Julian', 'Julien', 'Julio', 'Julius', 'Jupp', 'Juste', 'Justian', 'Justin', 'Justinian', 'Justus', 'Kaj', 'Kajetan', 'Kamillo', 'Karel', 'Karl', 'Karol', 'Karsten', 'Kary', 'Kasimir', 'Kaspar', 'Kay', 'Keith', 'Ken', 'Kenneth', 'Kersten', 'Kevin', 'Kilian', 'Kim', 'Kirsten', 'Klaas', 'Klaes', 'Klaudius', 'Klaus', 'Klemens', 'Klemenz', 'Knud', 'Knut', 'Konrad', 'Konradin', 'Konstantin', 'Kordt', 'Kornelius', 'Kristian', 'Kristof', 'Kristoffer', 'Kunibert', 'Kuno', 'Kunz', 'Kurt', 'Kyrill', 'Kyrillus', 'Kyros', 'Lajos', 'Lambert', 'Lamberto', 'Lambrecht', 'Lampert', 'Lamprecht', 'Larry', 'Lars', 'Latif', 'Laurens', 'Laurent', 'Laurenz', 'Laurenzo', 'Lauris', 'Lauro', 'Lawley', 'Leander', 'Leandro', 'Leandros', 'Leen', 'Leigh', 'Lembit', 'Lenas', 'Lenny', 'Lenz', 'Leo', 'Leon', 'Leonard', 'Leonardo', 'Leonello', 'Leonhard', 'Leontine', 'Leopold', 'Leopoldo', 'Lev', 'Lew', 'Lewis', 'Liam', 'Lienhard', 'Lino', 'Linus', 'Lion', 'Lionardo', 'Lionel', 'Livio', 'Livius', 'Lloyd', 'Lodewijk', 'Lorenz', 'Lorenzo', 'Loris', 'Lothair', 'Lothar', 'Lou', 'Louis', 'Lovis', 'Luc', 'Lucas', 'Luciano', 'Lucien', 'Lucio', 'Lucius', 'Ludewig', 'Ludovico', 'Ludvig', 'Ludvik', 'Ludwig', 'Ludwik', 'Luis', 'Luitpold', 'Lukas', 'Lutz', 'LuziusMaarten', 'Maicon', 'Malik', 'Manfred', 'Manfredo', 'Manoel', 'Manolo', 'Manuel', 'Marc', 'Marcel', 'Marcello', 'Marcellus', 'Marcelo', 'Marcial', 'Marco', 'Marcos', 'Marin', 'Marino', 'Marinus', 'Mario', 'Marius', 'Mark', 'Marko', 'Markus', 'Marlon', 'Marten', 'Martial', 'Martin', 'Martino', 'Marzell', 'Marzellus', 'Massimiliano', 'Mathias', 'Mathieu', 'Mathis', 'Matias', 'Matt', 'Matteo', 'Matthew', 'Matthias', 'Mattias', 'Mauritius', 'Mauritz', 'Maurizio', 'Mauro', 'Maurus', 'Max', 'Maxim', 'Maximilian', 'Maximilien', 'Meik', 'Michael', 'Michail', 'Michel', 'Mick', 'Mickey', 'Miguel', 'Mikael', 'Mikel', 'Milan', 'Mirco', 'Mirko', 'Miroslav', 'Miroslaw', 'Mitar', 'Morgan', 'Moritz', 'Moriz', 'Morris', 'Morten', 'Moufid', 'Mufid', 'Myron', 'Nabor', 'Nahor', 'Nat', 'Nathan', 'Nathanael', 'Nathaniel', 'Naveen', 'Neel', 'Nemo', 'Nevio', 'Nicholas', 'Nick', 'Nico', 'Nicolaas', 'Nicolas', 'Niels', 'Niklas', 'Niklaus', 'Niko', 'Nikolaj', 'Nikolaus', 'Nils', 'Noah', 'Noel', 'Norbert', 'Norberto', 'Norman', 'Normann', 'Notker', 'Noyan', 'Odin', 'Odo', 'Olek', 'Olindo', 'Olinto', 'Oliver', 'Olivier', 'Oliviero', 'Orlando', 'Oscar', 'Oskar', 'Osvaldo', 'Oswald', 'Oswaldo', 'Otello', 'Otfried', 'Othello', 'Othmar', 'Othon', 'Otmar', 'Ottfried', 'Ottmar', 'Otto', 'Ove', 'Pablo', 'Paco', 'Paddy', 'Palmiro', 'Pancho', 'Paolo', 'Pascal', 'Paschalis', 'Pascual', 'Pat', 'Patrick', 'Patrik', 'Patrizio', 'Patrizius', 'Paul', 'Pavel', 'Pawel', 'Pedro', 'Pepito', 'Per', 'Peter', 'Petter', 'Philemon', 'Philip', 'Philipp', 'Phillip', 'Piero', 'Pietro', 'Pius', 'Pjotr', 'Placido', 'Placidus', 'Pollux', 'Poul', 'Quentin', 'Quirin', 'Quirinus', 'Rafael', 'Raffaello', 'Ragnar', 'Raik', 'Raimondo', 'Raimund', 'Rainald', 'Rainer', 'Rainier', 'Ralf', 'Rando', 'Randolf', 'Randolph', 'Randulf', 'Randy', 'Raphael', 'Rasvan', 'Ray', 'Rayk', 'Raymond', 'Rayner', 'Razvan', 'Reginald', 'Reik', 'Reiko', 'Reimund', 'Reiner', 'Reinhard', 'Reinhold', 'Rembert', 'Remo', 'Renato', 'Renaud', 'Reto', 'Rex', 'Rhydian', 'Ricardo', 'Riccardo', 'Richard', 'Rick', 'Ricky', 'Rinaldo', 'Rivelino', 'Riziero', 'Rob', 'Robert', 'Roberto', 'Robin', 'Rod', 'Roderich', 'Roderick', 'Rodolfo', 'Rodrigo', 'Roger', 'Rojan', 'Roland', 'Rolando', 'Rolf', 'Romain', 'Roman', 'Romano', 'Romeo', 'Rowland', 'Roy', 'Rudger', 'Rudolf', 'Rudolph', 'Rudy', 'Rui', 'Rupert', 'Ruprecht', 'Ruud', 'Ruy', 'Sachso', 'Salomo', 'Salomon', 'Salvador', 'Salvator', 'Sam', 'Samir', 'Sammy', 'Samouel', 'Samuel', 'Sandro', 'Sasso', 'Saverio', 'Schorsch', 'Scott', 'Sebastian', 'Sebastiano', 'Sepp', 'Serenus', 'Sergei', 'Sergej', 'Sergio', 'Seth', 'Severiano', 'Severin', 'Severo', 'Shlomo', 'Sidonius', 'Siegbert', 'Siegfried', 'Sigfrid', 'Sigfrido', 'Sigisbert', 'Silas', 'Sileno', 'Silvain', 'Silvan', 'Silvano', 'Silvester', 'Silvestro', 'Silvian', 'Silvio', 'Silvius', 'Simeon', 'Simon', 'Solideo', 'Solomon', 'Stan', 'Stanislav', 'Stanislaw', 'Stanley', 'Stefan', 'Stefano', 'Steffen', 'Stepan', 'Stephan', 'Stephen', 'Steven', 'Stewart', 'Stuart', 'Sven', 'Svend', 'Sylvester', 'Szymon', 'Tammo', 'Tano', 'Taymour', 'Taymur', 'Teddy', 'Teo', 'Teobaldo', 'Teodoro', 'Thaer', 'Theo', 'Theobald', 'Theodor', 'Thibault', 'Thibaut', 'Thiemo', 'Thietmar', 'Thimo', 'Thomas', 'Thommy', 'Thorsten', 'Tiago', 'Tiberio', 'Tiberius', 'Til', 'Till', 'Tillman', 'Tillmann', 'Tilman', 'Tim', 'Tim', 'Timeon', 'Timm', 'Timmo', 'Timmy', 'Timo', 'Timon', 'Timoteo', 'Timotheus', 'Timothy', 'Tito', 'Titus', 'Tizian', 'Tiziano', 'Tobia', 'Tobiah', 'Tobias', 'Toby', 'Tom', 'Tomas', 'Tomaso', 'Tommaso', 'Tonio', 'Tony', 'Torsten', 'Uberto', 'Udo', 'Ugo', 'Ulf', 'Ulli', 'Ulric', 'Ulrich', 'Ulrico', 'Ulrik', 'Ulv', 'Umberto', 'Urbain', 'Urbano', 'Urs', 'Valente', 'Valentiano', 'Valentin', 'Valentino', 'Valerian', 'Valerio', 'Valerius', 'Veltin', 'Verner', 'Vernon', 'Vico', 'Victor', 'Viktor', 'Vilfredo', 'Vilhelm', 'Vincent', 'Vincenzo', 'Vinzenz', 'Vittorio', 'Viturin', 'Vivian', 'Viviano', 'Vladimir', 'Vladimiro', 'Volkard', 'Volker', 'Volkert', 'Volkhard', 'Volkmar', 'Waldemar', 'Walt', 'Walter', 'Walther', 'Warren', 'Welch', 'Werner', 'Wernher', 'Wieland', 'Wilfred', 'Wilfrid', 'Wilfried', 'Wilhelm', 'Wilibald', 'Willem', 'William', 'Willibald', 'Willy', 'Winston', 'Wladimir', 'Wolfgang', 'Xaver', 'Xavier', 'Yan', 'Yanick', 'Yanik', 'Yann', 'Yannick', 'Yitzhak', 'Yossi', 'Yves', 'Zach', 'Zacharias', 'Zachary']
surnames = ['Bexbach', 'Zwingenberg', 'Diez', 'Goslar', 'Haseluenne', 'Romrod', 'Wiesensteig', 'Meisenheim', 'Nagold', 'Gehrden', 'Seligenstadt', 'Schweinfurt', 'Niederkassel', 'Waldenburg', 'Woerrstadt', 'Duelmen', 'Muenster', 'Boppard', 'Wallduern', 'Erkrath', 'Straelen', 'Gudensberg', 'Wolkenstein', 'Ottweiler', 'Brueck', 'Huerth', 'Brilon', 'Hayingen', 'Waldenburg', 'Marktoberdorf', 'Schifferstadt', 'Wesenberg', 'Kroepelin', 'Neuenrade', 'Schneeberg', 'Ronneburg', 'Velden', 'Weilburg', 'Elstra', 'Offenburg', 'Neubulach', 'Kornwestheim', 'Gerolzhofen', 'Lauta', 'Osthofen', 'Mendig', 'Hennigsdorf', 'Bassum', 'Schillingsfuerst', 'Norden', 'Sayda', 'Roemhild', 'Tornesch', 'Winnenden', 'Eschwege', 'Freudenberg', 'Saarburg', 'Wittichenau', 'Kuppenheim', 'Frauenstein', 'Amoeneburg', 'Schkeuditz', 'Korschenbroich', 'Fulda', 'Oppenheim', 'Melsungen', 'Walsrode', 'Tegernsee', 'Hohnstein', 'Radevormwald', 'Ibbenbueren', 'Alsfeld', 'Rosenthal', 'Schwaigern', 'Ansbach', 'Hilpoltstein', 'Herrenberg', 'Liebstadt', 'Weinheim', 'Uhingen', 'Liebenau', 'Schwaan', 'Hohenmoelsen', 'Aub', 'Lehesten', 'Preetz', 'Lichtenberg', 'Erwitte', 'Adelsheim', 'Greussen', 'Kamen', 'Schlotheim', 'Barmstedt', 'Minden', 'Hettstedt', 'Neustrelitz', 'Wirges', 'Neckarsteinach', 'Goeppingen', 'Buedingen', 'Nideggen', 'Neubukow', 'Windischeschenbach', 'Scheer', 'Kupferberg', 'Daun', 'Beilstein', 'Dahlen', 'Golssen', 'Langen', 'Waghaeusel', 'Freudenberg', 'Burgdorf', 'Boehlen', 'Goldkronach', 'Roetha', 'Gelnhausen', 'Gehren', 'Spenge', 'Creussen', 'Wuppertal', 'Schluesselfeld', 'Fehmarn', 'Homburg', 'Ahlen', 'Wetzlar', 'Melle', 'Kelsterbach', 'Holzminden', 'Doebern', 'Niedernhall', 'Gefrees', 'Bruehl', 'Marl', 'Kaub', 'Miltenberg', 'Lorsch', 'Grimma', 'Bopfingen', 'Hauzenberg', 'Geldern', 'Dornstetten', 'Drensteinfurt', 'Buerstadt', 'Munster', 'Mellrichstadt', 'Vallendar', 'Marne', 'Hechingen', 'Murrhardt', 'Gefell', 'Pirmasens', 'Arneburg', 'Konz', 'Velburg', 'Nieheim', 'Waldheim', 'Ebermannstadt', 'Baesweiler', 'Reinbek', 'Engen', 'Pulsnitz', 'Burgstaedt', 'Grabow', 'Wriezen', 'Schrozberg', 'Maintal', 'Bruessow', 'Rodenberg', 'Rehau', 'Altena', 'Hirschberg', 'Marktheidenfeld', 'Georgsmarienhuette', 'Pegau', 'Oberwesel', 'Markranstaedt', 'Burgkunstadt', 'Barntrup', 'Zwiesel', 'Roesrath', 'Schildau', 'Waibstadt', 'Stoessen', 'Seeland', 'Stassfurt', 'Gunzenhausen', 'Todtnau', 'Burscheid', 'Beilngries', 'Mitterteich', 'Meissen', 'Herten', 'Fuerstenfeldbruck', 'Zeitz', 'Luckau', 'Arnis', 'Ludwigsstadt', 'Weissenberg', 'Hungen', 'Olfen', 'Zoeblitz', 'Warendorf', 'Kaiserslautern', 'Freyung', 'Bogen', 'Bergneustadt', 'Wittingen', 'Adenau', 'Eberswalde', 'Blumberg', 'Zirndorf', 'Muennerstadt', 'Linden', 'Neumuenster', 'Witzenhausen', 'Bretten', 'Zwenkau', 'Tanna', 'Beeskow', 'Buehl', 'Biedenkopf', 'Jarmen', 'Nidderau', 'Burghausen', 'Plauen', 'Barsinghausen', 'Lenzen', 'Nordhausen', 'Jena', 'Waldeck', 'Rottweil', 'Belgern', 'Doebeln', 'Juelich', 'Olpe', 'Burglengenfeld', 'Velten', 'Fellbach', 'Pfullendorf', 'Betzdorf', 'Weissenfels', 'Achim', 'Raunheim', 'Twistringen', 'Espelkamp', 'Northeim', 'Torgelow', 'Koelleda', 'Gommern', 'Loessnitz', 'Taucha', 'Merkendorf', 'Helmstedt', 'Heiligenhafen', 'Kyritz', 'Emsdetten', 'Putlitz', 'Kusel', 'Voelklingen', 'Ludwigslust', 'Frechen', 'Friesack', 'Marienmuenster', 'Schwabach', 'Herrnhut', 'Eschborn', 'Penzberg', 'Schoeningen', 'Rhinow', 'Waldbroel', 'Widdern', 'Pressath', 'Buetzow', 'Calw', 'Eibenstock', 'Rheinau', 'Graefenthal', 'Radeberg', 'Memmingen', 'Blieskastel', 'Joachimsthal', 'Grimmen', 'Bernsdorf', 'Graefenberg', 'Werdau','Rheinbach', 'Egeln', 'Neckarbischofsheim', 'Rochlitz', 'Alpirsbach', 'Arzberg', 'Ravenstein', 'Friedrichsdorf', 'Otterndorf', 'Hornburg', 'Dreieich', 'Neuss', 'Lichtenau', 'Radeburg', 'Eisfeld', 'Luetjenburg', 'Schwarzheide', 'Nordenham', 'Schoenau', 'Konstanz', 'Lauchheim', 'Hammelburg', 'Bergen', 'Felsberg', 'Hachenburg', 'Lengenfeld', 'Waltershausen', 'Wiehe', 'Gundelsheim', 'Elmshorn', 'Forchtenberg', 'Erbendorf', 'Bochum', 'Selb', 'Stadtprozelten', 'Waldenbuch', 'Westerstede', 'Paderborn', 'Guetzkow', 'Ulmen', 'Alzey', 'Osterburken', 'Kassel', 'Baunach', 'Freinsheim', 'Steinach', 'Pfreimd', 'Beerfelden', 'Ratingen', 'Schwelm', 'Lommatzsch', 'Otterberg', 'Viernheim', 'Landshut', 'Wanfried', 'Ilshofen', 'Wahlstedt', 'Griesheim', 'Schleusingen', 'Rodalben', 'Kamenz', 'Schalkau', 'Wolfach', 'Crailsheim', 'Edenkoben', 'Niebuell', 'Freystadt', 'Markgroeningen', 'Wildemann', 'Bergkamen', 'Schauenstein', 'Thannhausen', 'Loeningen', 'Volkmarsen', 'Arnsberg', 'Hof', 'Dargun', 'Marktsteft', 'Rain', 'Manderscheid', 'Kalkar', 'Lauterecken', 'Luegde', 'Sendenhorst', 'Kaarst', 'Schwentinental', 'Salzgitter', 'Roettingen', 'Friedrichstadt', 'Willebadessen', 'Niesky', 'Harsewinkel', 'Ennepetal', 'Kirtorf', 'Sondershausen', 'Hallenberg', 'Brackenheim', 'Owen', 'Niddatal', 'Braunlage', 'Viersen', 'Pfungstadt', 'Neusaess', 'Schleiden', 'Helmbrechts', 'Buttelstedt', 'Einbeck', 'Altenberg', 'Niederstetten', 'Grossenehrich', 'Stuehlingen', 'Burgbernheim', 'Guetersloh', 'Essen', 'Germering', 'Gransee', 'Selm', 'Teltow', 'Schrobenhausen', 'Norderstedt', 'Steinfurt', 'Neukirchen', 'ZoerbigZossen', 'Tangerhuette', 'Drolshagen', 'Donzdorf', 'Nittenau', 'Florstadt', 'Wallenfels', 'Fuerth', 'Ulrichstein', 'Tirschenreuth', 'Eilenburg', 'Wemding', 'Wuerzburg', 'Treuenbrietzen', 'Loehne', 'Klingenthal', 'Arnstadt', 'Moenchengladbach', 'Sebnitz', 'Mylau', 'Muenzenberg', 'Ziesar', 'Hamminkeln', 'Nauen', 'Aurich', 'Lieberose', 'Voehringen', 'Schopfheim', 'Saarlouis', 'Neuwied', 'Teublitz', 'Solingen', 'Moessingen', 'Luckenwalde', 'Lauchhammer', 'Muegeln', 'Werdohl', 'Grossalmerode', 'Parsberg', 'Burg', 'Hillesheim', 'Premnitz', 'Zwoenitz', 'Fuessen', 'Balve', 'Nortorf', 'Buedelsdorf', 'Nuernberg', 'Arnstein', 'Steinheim', 'Arnstein', 'Kyllburg', 'Zweibruecken', 'Wadern', 'Rosswein', 'Ballenstedt', 'Nettetal', 'Hornberg', 'Alsdorf', 'Eberbach', 'Spangenberg', 'Luetzen', 'Schlettau', 'Osnabrueck', 'Hueckelhoven', 'Dornhan', 'Starnberg', 'Waldkraiburg', 'Hermsdorf', 'Unterschleissheim', 'Grossraeschen', 'Ploen', 'Jerichow', 'Hockenheim', 'Spaichingen', 'Groeditz', 'Buxtehude', 'Gnoien', 'Brakel', 'Oppenau', 'Abenberg', 'Olsberg', 'Dieburg', 'Neresheim', 'Heilbronn', 'Asperg', 'Coesfeld', 'Monheim', 'Muellrose', 'Borgholzhausen', 'Ziegenrueck', 'Woldegk', 'Lollar', 'Lemgo', 'Finsterwalde', 'Putbus', 'Ochsenhausen', 'Knittlingen', 'Attendorn', 'Franzburg', 'Coburg', 'Herford', 'Lengefeld', 'Boeblingen', 'Krempe', 'Meiningen', 'Deggendorf', 'Ueckermuende', 'Seifhennersdorf', 'Peitz', 'Berlin', 'Werl', 'Penkun', 'Grafenau', 'Gedern', 'Vacha', 'Regen', 'Ranis', 'Haldensleben', 'Puettlingen', 'Vlotho', 'Waldmuenchen', 'Pottenstein', 'Aalen', 'Strausberg', 'Toenning', 'Neckargemuend', 'Schesslitz', 'Rieneck', 'Langenselbold', 'Rendsburg', 'Blomberg', 'Boxberg', 'Heide', 'Weingarten', 'Spremberg', 'Osterwieck', 'Kranichfeld', 'Unna', 'Oberkirch', 'Geisenheim', 'Eibelstadt', 'Greven', 'Bodenwerder', 'Leutershausen', 'Wolgast', 'Buttstaedt', 'Bischofswerda', 'Herzogenrath', 'Bielefeld', 'Rehna', 'Schwanebeck', 'Geiselhoering', 'Runkel', 'Lippstadt', 'Dinkelsbuehl', 'Krautheim', 'Sehnde', 'Schwetzingen', 'Brueel', 'Stadthagen', 'Gevelsberg', 'Ueberlingen', 'Leuna', 'Schwandorf', 'Worms', 'Rheinstetten', 'Elze', 'Rheinberg', 'Waldsassen', 'Goessnitz', 'Rahden', 'Erbach', 'Lindenfels', 'Langenhagen', 'Oberriexingen', 'Noerdlingen', 'Penig', 'Donauwoerth', 'Nastaetten', 'Heldrungen', 'Windsbach', 'Schotten', 'Crivitz', 'Ahaus', 'Riesa', 'Bruchsal', 'Wolfratshausen', 'Frohburg', 'Lichtenau', 'Niedenstein', 'Ochsenfurt', 'Rennerod', 'Stadtsteinach', 'Wunstorf', 'Schelklingen', 'Bensheim', 'Lohmar', 'Kaisersesch', 'Trebbin', 'Gifhorn', 'Richtenberg', 'Buergel', 'Angermuende', 'Herdecke', 'Kaltennordheim', 'Garding', 'Norderney', 'Duisburg', 'Langewiesen', 'Guestrow', 'Perleberg', 'Freital', 'Zschopau', 'Neuenstein', 'Netphen', 'Kandern', 'Neuruppin', 'Kuenzelsau', 'Aue', 'Seelow', 'Floeha', 'Grevesmuehlen', 'Immenhausen', 'Esens', 'Schoeppenstedt', 'Stolpen', 'Gera', 'Geilenkirchen', 'Creuzburg', 'Augsburg', 'Hadamar', 'Wuerselen', 'Barth', 'Schweich', 'Vilseck', 'Aschersleben', 'Suhl', 'Miesbach', 'Suessen', 'Barby', 'Gummersbach', 'Springe', 'Ochtrup', 'Meersburg', 'Oberlungwitz', 'Grafenwoehr', 'Poessneck', 'Genthin', 'Garbsen', 'Leutenberg', 'Tharandt', 'Haan', 'Wurzen', 'Sassenberg', 'Oberhof', 'Marienberg', 'Delmenhorst', 'Gladbeck', 'Tuttlingen', 'Karlstadt', 'Bottrop', 'Sonneberg', 'Stadtilm', 'Olbernhau', 'Moeckmuehl', 'Waldershof', 'Wildenfels', 'Aschaffenburg', 'Gerabronn', 'Hagenow', 'Vellmar', 'Celle', 'Wesseling', 'Meerbusch', 'Koblenz', 'Aulendorf', 'Spalt','Huenfeld', 'Wernigerode', 'Eckartsberga', 'Willich', 'Stade', 'Tengen', 'Pirna', 'Heideck', 'Wertingen', 'Hornbach', 'Koennern', 'Weissenstadt', 'Damme', 'Wiesloch', 'Emden', 'Freilassing', 'Varel', 'Dingolfing', 'Rietberg', 'Meppen', 'Dingelstaedt', 'Obermoschel', 'Trostberg', 'Telgte', 'Parchim', 'Weismain', 'Schwarzenbek', 'Wiehl', 'Weiterstadt', 'Zeven', 'Sprockhoevel', 'Bendorf', 'Stadtroda', 'Ruesselsheim', 'Kolbermoor', 'Sachsenhagen', 'Dassel', 'Syke', 'Ellingen', 'Hueckeswagen', 'Plochingen', 'Abensberg', 'Kulmbach', 'Bargteheide', 'Schmalkalden', 'Trochtelfingen', 'Besigheim', 'Hoya', 'Weissenthurm', 'Merseburg', 'Schluechtern', 'Babenhausen', 'Aach', 'Kremmen', 'Radebeul', 'Rosenfeld', 'Waldkirchen', 'Koeln', 'Flensburg', 'Bornheim', 'Gebesee', 'Gerlingen', 'Geisingen', 'Riedenburg', 'Velen', 'Laubach', 'Deidesheim', 'Zuelpich', 'Hoexter', 'Marlow', 'Ortenberg', 'Ortrand', 'Billerbeck', 'Elsterberg', 'Schneverdingen', 'Koenigsbrunn', 'Eltmann', 'Halberstadt', 'Butzbach', 'Illertissen', 'Gersthofen', 'Petershagen', 'Vilsbiburg', 'Lampertheim', 'Wehr', 'Sigmaringen', 'Schnaittenbach', 'Andernach', 'Mirow', 'Roding', 'Reinheim', 'Lauscha', 'Drebkau', 'Nordhorn', 'Amorbach', 'Herbstein', 'Hermeskeil', 'Moringen', 'Ettenheim', 'Winterberg', 'Niederstotzingen', 'Neckarsulm', 'Tuebingen', 'Berching', 'Tangermuende', 'Lucka', 'Pritzwalk', 'Goerlitz', 'Geisa', 'Stavenhagen', 'Weida', 'Stadtlengsfeld', 'Bremerhaven', 'Gruenberg', 'Ebeleben', 'Goldberg', 'Schwerte', 'Mainburg', 'Versmold', 'Eisenach', 'Bobingen', 'Wesselburen', 'Tauberbischofsheim', 'Michelstadt', 'Osterhofen', 'Muenchenbernsdorf', 'Korbach', 'Neukloster', 'Rudolstadt', 'Reutlingen', 'Erkner', 'Messstetten', 'Bayreuth', 'Falkensee', 'Wegeleben', 'Weener', 'Pulheim', 'Ravensburg', 'Schoenewalde', 'Ditzingen', 'Eichstaett', 'Roth', 'Graefenhainichen', 'Brandis', 'Leisnig', 'Kloetze', 'Meyenburg', 'Monschau', 'Ehrenfriedersdorf', 'Burgwedel', 'Gelsenkirchen', 'Solms', 'Waischenfeld', 'Philippsburg', 'Schiltach', 'Bleicherode', 'Geithain', 'Detmold', 'Lorch', 'Netzschkau', 'Peine', 'Hemmoor', 'Siegburg', 'Dahn', 'Trendelburg', 'Plattling', 'Wittlich', 'Warstein', 'Erding', 'Elsterwerda', 'Wilthen', 'Pasewalk', 'Erlensee', 'Stadtlohn', 'Mosbach', 'Tettnang', 'Colditz', 'Tecklenburg', 'Stendal', 'Wildberg', 'Mindelheim', 'Wasungen', 'Soemmerda', 'Wegberg', 'Wittenburg', 'Sonnewalde', 'Ludwigsburg', 'Obernkirchen', 'Kehl', 'Gardelegen', 'Leonberg', 'Ingelfingen', 'Emmendingen', 'Wittenberge', 'Rees', 'Gueglingen', 'Forchheim', 'Laupheim', 'Lebus', 'Ebersberg', 'Backnang', 'Feuchtwangen', 'Bocholt', 'Marktbreit', 'Gaggenau', 'Schoenwald', 'Bleckede', 'Krefeld', 'Hecklingen', 'Nossen', 'Wuelfrath', 'Welzow', 'Boennigheim', 'Hartha', 'Erkelenz', 'Altenau', 'Rheinboellen', 'Nidda', 'Friedland', 'Rathenow', 'Koenigswinter', 'Karlsruhe', 'Prenzlau', 'Darmstadt', 'Kaufbeuren', 'Templin', 'Datteln', 'Kitzingen', 'Dorfen', 'Mahlberg', 'Moeckern', 'Delitzsch', 'Hersbruck', 'Groitzsch', 'Kellinghusen', 'Heilsbronn', 'Weinsberg', 'Lage', 'Luebtheen', 'Meinerzhagen', 'Senftenberg', 'Muellheim', 'Dueren', 'Renningen', 'Dinklage', 'Kierspe', 'Sinsheim', 'Kitzscher', 'Delbrueck', 'Augustusburg', 'Goettingen', 'Soest', 'Kirchhain', 'Dortmund', 'Hattingen', 'Pattensen', 'Oderberg', 'Muehltroff', 'Altenburg', 'Chemnitz', 'Guesten', 'Rhede', 'Husum', 'Thale', 'Luedinghausen', 'Dorsten', 'Friedrichsthal', 'Malchin', 'Pfullingen', 'Elterlein', 'Volkach', 'Friedrichshafen', 'Gernsheim', 'Hemau', 'Erlangen', 'Lengerich', 'Lorch', 'Coswig', 'Rossleben', 'Rastatt', 'Lehrte', 'Eckernfoerde', 'Rastenberg', 'Prichsenstadt', 'Gruenstadt', 'Cuxhaven', 'Neunkirchen', 'Oschatz', 'Ennigerloh', 'Vohenstrauss', 'Passau', 'Leipzig', 'Ostritz', 'Katzenelnbogen', 'Dassow', 'Greiz', 'Uslar', 'Mansfeld', 'Oberkochen', 'Beckum', 'Breuberg', 'Sangerhausen', 'Kleve', 'Herdorf', 'Havelsee', 'Hagen', 'Nabburg', 'Mannheim', 'Altensteig', 'Toenisvorst', 'Dietenheim', 'Mittweida', 'Kemnath', 'Heubach', 'Borgentreich', 'Cochem', 'Hildburghausen', 'Kirchheimbolanden', 'Schenefeld', 'Merzig', 'Burgau', 'Rodgau', 'Luedenscheid', 'Marsberg', 'Bredstedt', 'Glashuette', 'Herrieden', 'Laichingen', 'Freren', 'Taunusstein', 'Bueckeburg', 'Giessen', 'Ruethen', 'Landsberg', 'Dietzenbach', 'Trossingen', 'Gerbstedt', 'Kraichtal', 'Markdorf', 'Loewenstein', 'Wolfhagen', 'Rauenberg', 'Gengenbach', 'Kronach', 'Waldkappel', 'Hettingen', 'Calau', 'Huefingen', 'Eutin', 'Markneukirchen', 'Duderstadt', 'Braunfels', 'Aachen', 'Geringswalde', 'Wassenberg', 'Magdala', 'Salzkotten', 'Eschershausen', 'Puchheim', 'Kreuztal', 'Kindelbrueck', 'Neukalen', 'Voehrenbach', 'Bueren', 'Wermelskirchen', 'Gladenbach', 'Kuehlungsborn', 'Asslar', 'Overath', 'Emmelshausen', 'Schoenberg', 'Tribsees', 'Cloppenburg', 'Lunzenau', 'Dillenburg', 'Stutensee', 'Remscheid', 'Meckenheim', 'Braunsbedra', 'Pleystein', 'Oberviechtach', 'Albstadt', 'Kirchberg', 'Creglingen', 'Stromberg', 'Enger', 'Weinstadt', 'Rheinsberg', 'Buchloe', 'Schoemberg', 'Vechta', 'Vienenburg', 'Waiblingen', 'Geislingen', 'Messkirch', 'Hildesheim', 'Speyer', 'Oerlinghausen', 'Kirchenlamitz', 'Teterow', 'Cham', 'Ladenburg', 'Wertheim', 'Niemegk', 'Bremervoerde', 'Zierenberg', 'Witten', 'Grossenhain', 'Heimbach', 'Kempen', 'Recklinghausen', 'Ruhland', 'Rothenfels', 'Werne', 'Pegnitz', 'Kemberg', 'Schwarzenborn', 'Herbolzheim', 'Osterfeld', 'Geisenfeld', 'Wolmirstedt', 'Markkleeberg', 'Kastellaun', 'Haigerloch', 'Ratzeburg', 'Torgau', 'Freudenstadt', 'Kevelaer', 'Sulingen', 'Riedstadt', 'Zwickau', 'Hausach', 'Herborn', 'Koenigsbrueck', 'Halver', 'Plettenberg', 'Eggenfelden', 'Loerrach', 'Bedburg', 'Quakenbrueck', 'Soltau', 'Dohna', 'Neuoetting', 'Leipheim', 'Geretsried', 'Stadtallendorf', 'Hoerstel', 'Walldorf', 'Weissensee', 'Borna', 'Metzingen', 'Laufen', 'Freising', 'Bergheim', 'Eschweiler', 'Guben', 'Breckerfeld', 'Loeffingen', 'Hameln', 'Tessin', 'Kelheim', 'Harzgerode', 'Meldorf', 'Stadtoldendorf', 'Wurzbach', 'Luebz', 'Mengen', 'Elsfleth', 'Dierdorf', 'Friedberg', 'Altentreptow', 'Glinde', 'Iphofen', 'Laatzen', 'Langelsheim', 'Hardegsen', 'Oberasbach', 'Oberwiesenthal', 'Amberg', 'Grossschirma', 'Schwalmstadt', 'Aichtal', 'Rhens', 'Rauschenberg', 'Marktleuthen', 'Bockenem', 'Muehlacker', 'Baunatal', 'Lahnstein', 'Naumburg', 'Ichenhausen', 'Trier', 'Neudenau', 'Dinslaken', 'Bamberg', 'Vellberg', 'Hirschau', 'Ludwigsfelde', 'Naila', 'Groeningen', 'Themar', 'Glueckstadt', 'Gaildorf', 'Weissenhorn', 'Geesthacht', 'Waechtersbach', 'Pruem', 'Herzogenaurach', 'Fritzlar', 'Glauchau', 'Schriesheim', 'Muencheberg', 'Eisenberg', 'Heinsberg', 'Waltrop', 'Hallstadt', 'Iserlohn', 'Friesoythe', 'Langenzenn', 'Herne', 'Hanau', 'Borkum', 'Westerburg', 'Stockach', 'Eisenhuettenstadt', 'Geseke', 'Papenburg', 'Leverkusen', 'Marburg', 'Dettelbach', 'Wolfenbuettel', 'Neuenbuerg', 'Sassnitz', 'Guenzburg', 'Schnackenburg', 'Schramberg', 'Gescher', 'Uelzen', 'Hamm','Aichach', 'Rosenheim', 'Ostfildern', 'Plaue', 'Seelze', 'Buende', 'Sachsenheim', 'Wedel', 'Welzheim', 'Tittmoning', 'Fuerstenau', 'Meschede', 'Lennestadt', 'Euskirchen', 'Ellrich', 'Olching', 'Kluetz', 'Rinteln', 'Obertshausen', 'Schkoelen', 'Laage', 'Roetz', 'Brunsbuettel', 'Ulm', 'Selbitz', 'Havelberg', 'Hemsbach', 'Wissen', 'Dippoldiswalde', 'Rabenau', 'Gruensfeld', 'Bautzen', 'Schleswig', 'Itzehoe', 'Waldkirch', 'Kandel', 'Mainbernheim', 'Hainichen', 'Balingen', 'Weikersheim', 'Nuertingen', 'Beelitz','Renchen', 'Burladingen', 'Sarstedt', 'Kahla', 'Wesel', 'Sindelfingen', 'Leun', 'Altlandsberg', 'Rockenhausen', 'Borken', 'Kroppenstedt', 'Schraplau', 'Holzgerlingen', 'Montabaur', 'Usedom', 'Bersenbrueck', 'Baiersdorf', 'Eppelheim', 'Kaltenkirchen', 'Lychen', 'Crimmitschau', 'Alzenau', 'Bruchkoebel', 'Troisdorf', 'Schoensee', 'Penzlin', 'Wolfstein', 'Kirn', 'Oestringen', 'Blaubeuren', 'Lichtenfels', 'Annaburg', 'Usingen', 'Hoyerswerda', 'Wittenberg', 'Verl', 'Braubach', 'Thum', 'Hohenleuben', 'Braunschweig', 'Warin', 'Filderstadt', 'Wilster', 'Wolfsburg', 'Loitz', 'Dachau', 'Biesenthal', 'Landstuhl', 'Meuselwitz', 'Schmallenberg', 'Hassfurt', 'Oelde', 'Birkenfeld', 'Hofgeismar', 'Donaueschingen', 'Triptis', 'Lichtenfels', 'Naunhof', 'Wipperfuerth', 'Viechtach', 'Siegen', 'Luebbecke', 'Beverungen', 'Oehringen', 'Luenen', 'Horstmar', 'Erftstadt', 'Rheine', 'Strehla', 'Zittau', 'Maulbronn', 'Allstedt', 'Munderkingen', 'Stein', 'Heitersheim', 'Sesslach', 'Pocking', 'Baernau', 'Dransfeld', 'Altoetting', 'Pforzheim', 'Baumholder', 'Eggesin', 'Neuerburg', 'Lassan', 'Werneuchen', 'Goch', 'Bramsche', 'Isselburg', 'Marktredwitz', 'Grebenau', 'Mettmann', 'Kuelsheim', 'Regensburg', 'Ronnenberg', 'Wittmund', 'Neubrandenburg', 'Schuettorf', 'Langenburg', 'Rutesheim', 'Mittenwalde', 'Hartenstein', 'Gotha', 'Straubing', 'Malchow', 'Neuenhaus', 'Elzach', 'Langenau', 'Schlieben', 'Friedrichroda', 'Schmoelln', 'Zehdenick', 'Wilsdruff', 'Teuchern', 'Rodewisch', 'Ohrdruf', 'Braeunlingen', 'Schwabmuenchen', 'Herbrechtingen', 'Heiligenhaus', 'Muensingen', 'Pappenheim', 'Velbert', 'Wunsiedel', 'Kenzingen', 'Vreden', 'Idstein', 'Oranienburg', 'Mayen', 'Wiesmoor', 'Oberhausen', 'Scheinfeld', 'Bitburg', 'Haiger', 'Treuchtlingen', 'Kappeln', 'Heimsheim', 'Riedlingen', 'Staufenberg', 'Hagenbach', 'Treffurt', 'Lich', 'Schleiz', 'Gerolstein', 'Sternberg', 'Dormagen', 'Sinzig', 'Sulzburg', 'Muenstermaifeld', 'Neumark', 'Elsdorf', 'Grossbottwar', 'Pinneberg', 'Freiberg', 'Gammertingen', 'Stadtbergen', 'Seesen', 'Ebern', 'Ruhla', 'Warburg', 'Rerik', 'Hemer', 'Geyer', 'Senden', 'Muenchberg', 'Treuen', 'Hilden', 'Liebenwalde', 'Achern', 'Jueterbog', 'Leimen', 'Betzenstein', 'Bacharach', 'Haiterbach', 'Fladungen', 'Ahrensburg', 'Grevenbroich', 'Mechernich', 'Hemmingen', 'Karben', 'Schlitz', 'Grossbreitenbach', 'Grossroehrsdorf', 'Gadebusch', 'Wassertruedingen', 'Nassau']


def genGiven(sex, iterations):
	'Vornamen erzeugen'
	
	global nmale, nfemale
	
	if sex == 0:
		ls = nmale
	elif sex == 1:
		ls = nfemale
	return genName(ls, iterations)

def genSurname(iterations):
	global surnames
	return genName(surnames, iterations)


def genName(ls, iterations):
	'Namen erzeugen'
	
	re = outOf(ls)
	for i in range(iterations):
		re = shakeName(re)
	return re
	

def shakeName(name):
	'Namen leicht verändern'
	
	cons = 'bcdfghjklmnpqrstvwxz'
	vowels = 'aeiouy'
	CONS = 'BCDFGHJKLMNPQRSTVWXZ'
	VOWELS = 'AEIOUY'
	abc = (cons, vowels, CONS, VOWELS)
	CHANGENESS = 10 #In Prozent
	digraphs = ['sch', 'ch', 'ck', 'st', 'sp', 'qu']
	re = ''
	
	while name:
		if name[0:2] in digraphs:
			i = name[0:2]
			name = name[2:]
		elif name[0:3] in digraphs:
			i = name[0:3]
			name = name[3:]
		else:
			i = name[0]
			name = name[1:]
			
		if randint(1, 100) <= CHANGENESS:
			for charClass in abc:
				if i[0] in charClass:
					re += outOf(charClass)
					break
		else:
			re += i
			
	if randint(1, 100) <= CHANGENESS:
		re = re[: - 1]
	if randint(1, 100) <= CHANGENESS:
		if re[- 1] in cons:
			re += outOf(vowels)
		elif re[- 1] in vowels:
			re += outOf(cons)
			
	return re



people = []
living = []
msingles = []
fsingles = []


class Person():
	global living
	global people
	global msingles
	global fsingles
	
	population = 0
	DAYSPERYEAR = 365
	
	
	def __init__(self, birth, father, mother, place, sex = - 1, given = None, nameObscurity = 2):
		self.father = father
		self.mother = mother
		self.genes = {}
		self.yieldGenes()
		self.num = Person.population
		self.place = place
		Person.population += 1
		self.birth = birth
		
		if sex == 1:
			self.genes['XY'] = (True, True)
		elif sex == 0:
			self.genes['XY'] = (True, False)
		if self.genes['XY'] == (True, True):
			self.sex = True		#f
		else:
			self.sex = False	#m
				
		if given == None:
			self.given = genGiven(self.sex, nameObscurity)
		else:
			self.given = given
		
		tradition = self.getFamilyNames()
		if len(tradition) > 0 and randint(0, 1) > 0:
			self.given = outOf(tradition)
		
		self.bannermen = []
		self.liegeLord = None
		self.subjects = []
		self.subjectTo = []
		self.death = None
		self.married = False
		self.currentlyMarried = False
		self.weddings = []
		self.spouses = []
		self.children = []
		self.rule = None
		if self.father == None:
			self.name = genSurname(nameObscurity)
		else:
			self.name = self.father.getSurname()
		
		if self.sex == 0:
			msingles.append(self)
		else:
			fsingles.append(self)
		living.append(self)
		people.append(self)
	
	
	def getGenes(self):
		return self.genes
		
	
	def yieldGenes(self):
		#Angaben zur Häufigkeit in Prozent
		CHROMOPROBS = {
			'XY'				: (50,'xy'),
			'dis-albinism'		: (1,  'r'),
			'dis-alzheimer'		: (30, 'D'),
			'dis-epilepsy'		: (2,  'r'),
			'dis-hemophily'		: (3, 'xr'),
			'dis-impotence'		: (12, 'r'),
			'dis-lackwit'		: (8,  'D'),
			
			'hair-curls'		: (15, 'i'),
			'hair-persistency'	: (20, 'i'),
			'hair-blackness'	: (80, 'i'),
			'hair-redness'		: (60, 'i'),
			
			'face-broadness'	: (50, 'i'),
			'face-overbite'		: (3,  'D'),
			'face-underbite'	: (2,  'D'),
			
			'nose-broadness'	: (40, 'i'),
			'nose-length'		: (40, 'i'),
			'nose-hook'			: (2,  'D'),
			
			'ear-freelobe'		: (40, 'D'),
			'ear-sails'			: (40, 'r'),
			
			'eye-width'			: (40, 'D'),
			'eye-height'		: (40, 'D'),
			'eye-blueness'		: (40, 'D'),
			'eye-nonbrownness'	: (96, 'r'),
			'eye-browlength'	: (60, 'D'),
			'eye-browbroadness'	: (4,  'r')
			
		}
		if self.father == None:
			for i in CHROMOPROBS.keys():
				if randint(1, 100) <= CHROMOPROBS[i][0]:
					self.genes[i] = (True, True)
					if CHROMOPROBS[i][1] == 'xr':
						if self.genes['XY'] == (True, True):
							self.genes[i] == (True, False)
						self.genes[i] = (True, True)
				else:
					self.genes[i] = (False, False)
		else:
			father = self.father.getGenes()
			mother = self.mother.getGenes()
			genes = {}
			for i in father.keys():
				f = outOf(father[i])
				m = outOf(mother[i])
				genes[i] = (f, m)
	
	
	def data(self):
		'Gibt das Datenblatt einer Person zurueck'
		
		re = """
		%s (%s)
		%s - %s
		Vater: %s
		Mutter: %s
		""" % (self, "mw"[self.sex], self.birth / Person.DAYSPERYEAR, self.death / Person.DAYSPERYEAR, self.father, self.mother)
		
		if self.married:
			re += "Partner:\n"
			for i in range(len(self.spouses)):
				re += "                " + str(self.weddings[i] / Person.DAYSPERYEAR) + "   " + str(self.spouses[i]) + "\n"
			
			re += "                Kinder:\n"
			for i in self.children:
				re += "                " + str(i.birth / Person.DAYSPERYEAR) + "   " + str(i) + "\n"
		
		if not self.liegeLord == None:
			re += "\n\nLehensherr: %s" % self.liegeLord
		
		if len(self.subjectTo) > 1 or (self.subjectTo and self.liegeLord != None):
			re += "\n\nHerrscher:"
		for n, i in enumerate(self.bannermen):
			re += "  %s - %s" % (n, i)
		
		if self.subjects:
			re += "\n\nUntertanen: %s" % len(self.subjects)
		
		if self.bannermen:
			re += "\n\nGefolgsleute:"
		for i in self.bannermen:
			re += "  - " + i
		return re
	
	
	def __str__(self):
		if self.death == None:
			if not self.rule == None:
				return '%s - %s %s von %s (*%s)' % (self.num, self.given, self.name, self.rule, self.birth / Person.DAYSPERYEAR)
			return '%s - %s %s (*%s)' % (self.num, self.given, self.name, self.birth / Person.DAYSPERYEAR)
		if not self.rule == None:
			return '%s - %s %s von %s (%s - %s)' % (self.num, self.given, self.name, self.rule, self.birth / Person.DAYSPERYEAR, self.death / Person.DAYSPERYEAR)
		return '%s - %s %s (%s - %s)' % (self.num, self.given, self.name, self.birth / Person.DAYSPERYEAR, self.death / Person.DAYSPERYEAR)
	
	
	def getAge(self, day):
		return (day - self.birth) / Person.DAYSPERYEAR
		
	
	def getBirth(self):
		return self.birth / Person.DAYSPERYEAR
	
	
	def getSex(self):
		return self.sex


	def getGiven(self):
		return self.given
	
	
	def getFamilyNames(self):
		ego = self
		try:
			if self.sex == 0:
				names = [self.mother.father.getGiven()]
			else:
				names = [self.father.mother.getGiven()]
		except:
			names = []
		while True:
			try:
				if self.sex == 0:
					ego = ego.father
				else:
					ego = ego.mother
				names.append(ego.getGiven())
			except:
				return names
	
	
	def getRule(self):
		return self.rule
	
	
	def setRule(self, city):
		self.rule = city
	
	
	def getSubRule(self, n = 0):
		re = [(n, self)]
		for i in self.bannermen:
			re += i.getSubRule(n + 1)
		return re
	
	
	def strRule(self):
		re = "Graf %s %s von %s\n" % (self.given, self.name, str(self.rule))
		for i in self.getSubRule():
			re += "\t" * i[0]
			p = i[1]
			re += str(p)
			if not p.getRule() == None:
				re += ",   " + str(p.getRule())
			re += "\n"
		return re
		
	
	def getSurname(self):
		'Gibt den Nachnamen einer Person zurueck'
		
		return self.name
	
	
	def isMarried(self):
		return self.currentlyMarried
	
	
	def marry(self, spouse, day):
		self.spouses.append(spouse)
		self.weddings.append(day)
		self.married = True
		self.currentlyMarried = True
		try:
			msingles.remove(self)
		except ValueError:
			fsingles.remove(self)
	
	
	def getSpouse(self):
		return self.spouses[- 1]
	
	
	def careless(self, child):
		self.children.append(child)
	
	
	def getChildren(self):
		return len(self.children)
	
	
	def getFirstGradeRelatives(self):
		'Gibt die Eltern und Kinder einer Person zurueck'
		
		re = []
		if not self.father == None:
			re.append(self.father)
		if not self.mother == None:
			re.append(self.mother)
		for i in self.children:
			re.append(i)
		return re
	
	
	def detGrade(self, person):
		grade = 0
		relatives = [self]
		while grade < 4:
			next = []
			grade += 1
			for i in relatives:
				try:
					next += i.getFirstGradeRelatives()
				except:
					continue
			for i in next:
				if i not in relatives:
					relatives.append(i)
			if person in relatives:
				return grade
		return 4
			

	def die(self, day):
		self.death = day
		if self.currentlyMarried:
			self.getSpouse().currentlyMarried = False
			if self.sex == 0:
				fsingles.append(self.getSpouse())
			else:
				msingles.append(self.getSpouse())
		else:
			try:
				msingles.remove(self)
			except ValueError:
				fsingles.remove(self)
		'''if self in kings:
			#print "King dead"
			try:
				#print "Searching for successor"
				kings.append(self.getSuccessor(self.death))
			except AttributeError:
				kings.append(self.getSuccessor(self.death, False))'''
		living.remove(self)
	
	
	def getDeath(self):
		return self.death / Person.DAYSPERYEAR
	
	
	def getSuccessor(self, day, salic = True):
		'Gibt den Nachfolger eines Regenten an.'
		
		if self.death == None:
			return self.death
		
		rels = self.getFirstGradeRelatives()
		
		for c in range(5):
			livingNow = []
			
			for i in rels:
				if i == None:
					continue
				if (day - i.birth) / Person.DAYSPERYEAR > 16 + randint(- 2, 2) and (day < i.death or i.death == None):
					livingNow.append((i.birth, i))
			livingNow.sort()
			for i in livingNow:
				#print salic, i[1].sex == 1, (salic and i[1].sex == 1)
				if not(salic and i[1].sex == 1):
					return i[1]
			next = []
			for i in rels:
				next += i.getFirstGradeRelatives()
			for i in next:
				if i not in rels:
					rels.append(i)
		return None
	
	
	def printDescendants(self, indent, generations = 100):
		if generations >= 0:
			print "|\t" * indent, "|------", self
			for i in self.children:
				i.printDescendants(indent + 1, generations - 1)
			for i in self.spouses:
				print "|\t" * (indent + 1), "  oo", i
	
	
	def printAncestors(self, indent, both = True, generations = 100):
		if generations >= 0:
			if not both:
				indent = 0
			if not self.father == None:
				self.father.printAncestors(indent + 1, both, generations - 1)
			print "\t" * indent, self
			if not self.mother == None and both:
				self.mother.printAncestors(indent + 1, both, generations - 1)
	
	
	def pledge(self, subject, bannerman = False):
		if bannerman:
			self.bannermen.append(subject)
			subject.liegeLord = self
		self.subjects.append(subject)
		subject.subjectTo.append(self)

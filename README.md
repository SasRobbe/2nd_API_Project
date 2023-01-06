# **ReadMe Project-ApiDev**
## _Robbe Sas 2ccs01_
* ### gekozen thema
  > Deze Api is gebouwd rond het thema lootboxes binnen gaming. Tegenover vroeger game ik zeer weinig, maar dit weerhoudt niet dat gamen een stuk van mijn jeugd is geweest. De Api focust zich vooral op het "lootbox" aspect binnen games. de Api kan lootboxes aanmaken en hier items aan verbinden, zo is het dus mogelijk om uw eigen lootbox samen te stellen. Ook heb ik ervoor gekozen om heroes toe te voegen. Hiermee heb ik hashing en authenication mee uitgevoerd.
  >
  > Ik heb me gehouden bij de algemene eisen van dit project. Dit betekent dus dat ik ervoor gekozen heb om geen extra uitrbreiden toe te voegen.

* ### links
hosted Api: https://system-service-sasrobbe.cloud.okteto.net/

* ### end-points
#### GET
  * /lootboxes : Lees alle lootboxes (heeft auth)
  * /lootboxes/{lootbox_id} : Lees een specifieke lootbox aan de hand van een id
  * /items : Lees alle items
  * /heroes : Lees alle heroes
#### POST
  * /lootboxes : Maak een nieuwe lootbox aan
  * /lootboxes/{lootbox_id}/items : Maak een nieuwe item aan voor een lootbox
  * /heroes : Maak een nieuwe hero aan door deze een naam + secret(hashed) te geven
  * (/token : Gebruikt om authentication mee uit te voeren)
#### PUT
  * /heroes/{id} : Pas de naam van een specifieke hero aan
#### DELETE
  * /heroes{id} : Verwijder een specifieke hero

* ### Postman screenshots
  * #### Get Lootboxes
  ![Lootboxes get]()
  * #### Post Lootboxes
  ![Lootboxes post](https://i.imgur.com/K2wA3l5.png)
  * #### Get specific Lootbox
  ![Lootboxes get specific](https://i.imgur.com/w34ReYx.png)
  * #### Post Item for Lootbox
  ![Lootboxes post Item](https://i.imgur.com/tfRBj4D.png)
  ![Item proof](https://i.imgur.com/dwRSIf3.png)
  * #### Get Items
  ![Items get](https://i.imgur.com/9nAKP7B.png)
  * #### Get Heroes
  ![Heroes get](https://i.imgur.com/doomwux.png)
  * #### Post Heroes
  ![Heroes post](https://i.imgur.com/PhSrJJK.png)
  * #### Update a Hero
  ![Heroes put](https://i.imgur.com/utOx6aD.png)
  * #### Delete a hero
  ![Heroes delete](https://i.imgur.com/Suid8ck.png)
  
* ### OpenAPI Docs
![Image api docs](https://i.imgur.com/zG1mp95.png)

* ### Authentication
![Auth](https://i.imgur.com/clfpQ8x.png)

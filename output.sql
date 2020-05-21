insert all
into permissions values ('standard')
into permissions values ('chat')
into permissions values ('essentials')
into permissions values ('kit')
into permissions values ('kit_tools')
into permissions values ('kit_profession')
into permissions values ('afk')
into permissions values ('home_kit')
into permissions values ('set_home')
into permissions values ('warp_home')
into permissions values ('del_home')
into permissions values ('ping')
into permissions values ('rules')
into permissions values ('tpa')
into permissions values ('tpaccept')
into permissions values ('tpdeny')
into permissions values ('tpahere')
into permissions values ('balance')
into permissions values ('time')
into permissions values ('moderator')
into permissions values ('kick')
into permissions values ('give')
into permissions values ('gamemode')
into permissions values ('kill')
into permissions values ('admin')
into permissions values ('ban')
into permissions values ('ban_ip')
into permissions values ('op')
into permissions values ('deop')
into permissions values ('faction_leader')
into permissions values ('faction_member')
select * from dual;
/* RESPONSE STATUS:  200  */
insert all
into players(name) values('VaderVizsla')
into players(name) values('AbrahamLincoln')
into players(name) values('newhalen')
into players(name) values('KunSing')
into players(name) values('zuckusschewbacca')
into players(name) values('lionel')
into players(name) values('CalvinCoolidge')
into players(name) values('mervyn')
into players(name) values('carmen')
into players(name) values('TanoBane')
into players(name) values('abbie')
into players(name) values('woodville')
into players(name) values('khalid')
into players(name) values('rhian')
into players(name) values('LyndonBJohnson')
into players(name) values('preslie')
into players(name) values('bobalando')
into players(name) values('sebulbayoda')
into players(name) values('WoodrowWilson')
into players(name) values('caterina')
select * from dual;
/* RESPONSE STATUS:  200  */
insert all
into items(item_name,item_description) values('Air','Some honest air')
into items(item_name,item_description) values('Stone','An awesome stone')
into items(item_name,item_description) values('Granite','Show it to your friends. Your granite')
into items(item_name,item_description) values('Polished Granite','An elementary polished granite')
into items(item_name,item_description) values('Diorite','Pure diorite')
into items(item_name,item_description) values('Polished Diorite','A decent looking polished diorite')
into items(item_name,item_description) values('Andesite','Funny looking andesite')
into items(item_name,item_description) values('Polished Andesite','Has no wheels, but its a decent polished andesite')
into items(item_name,item_description) values('Grass','Pretty nice grass')
into items(item_name,item_description) values('Dirt','An ordinary dirt')
into items(item_name,item_description) values('Coarse Dirt','An everyday coarse dirt')
into items(item_name,item_description) values('Podzol','Your average podzol')
into items(item_name,item_description) values('Cobblestone','Mainstream cobblestone')
into items(item_name,item_description) values('Oak Wood Plank','A beautiful oak wood plank')
into items(item_name,item_description) values('Spruce Wood Plank','A serious looking spruce wood plank')
into items(item_name,item_description) values('Birch Wood Plank','Unique birch wood plank')
into items(item_name,item_description) values('Jungle Wood Plank','An elementary jungle wood plank')
into items(item_name,item_description) values('Acacia Wood Plank','A nice acacia wood plank')
into items(item_name,item_description) values('Dark Oak Wood Plank','An elementary dark oak wood plank')
into items(item_name,item_description) values('Oak Sapling','Funny looking oak sapling')
into items(item_name,item_description) values('Spruce Sapling','A beautiful spruce sapling')
into items(item_name,item_description) values('Birch Sapling','A rare birch sapling')
into items(item_name,item_description) values('Jungle Sapling','A common jungle sapling')
into items(item_name,item_description) values('Acacia Sapling','A common acacia sapling')
into items(item_name,item_description) values('Dark Oak Sapling','A piece of cake but its actually dark oak sapling')
into items(item_name,item_description) values('Bedrock','An awesome bedrock')
into items(item_name,item_description) values('Flowing Water','Close your eyes again, its still just one more flowing water')
into items(item_name,item_description) values('Still Water','A rare still water')
into items(item_name,item_description) values('Flowing Lava','Has no wheels, but its a decent flowing lava')
into items(item_name,item_description) values('Still Lava','Looks better than you, a good still lava')
into items(item_name,item_description) values('Sand','How did you even get this sand')
into items(item_name,item_description) values('Red Sand','A rare red sand')
into items(item_name,item_description) values('Gravel','A pretty cool gravel')
into items(item_name,item_description) values('Gold Ore','A standard gold ore')
into items(item_name,item_description) values('Iron Ore','A neat iron ore')
into items(item_name,item_description) values('Coal Ore','A conventional coal ore')
into items(item_name,item_description) values('Oak Wood','Has no wheels, but its a decent oak wood')
into items(item_name,item_description) values('Spruce Wood','Standard spruce wood')
into items(item_name,item_description) values('Birch Wood','A f*cking birch wood')
into items(item_name,item_description) values('Jungle Wood','Your usual jungle wood')
into items(item_name,item_description) values('Oak Leaves','Simple oak leaves')
into items(item_name,item_description) values('Spruce Leaves','An average spruce leaves')
into items(item_name,item_description) values('Birch Leaves','A common birch leaves')
into items(item_name,item_description) values('Jungle Leaves','Go crazy with this jungle leaves')
into items(item_name,item_description) values('Sponge','A coherent sponge')
into items(item_name,item_description) values('Wet Sponge','A sarcastic wet sponge')
into items(item_name,item_description) values('Glass','Unique glass')
into items(item_name,item_description) values('Lapis Lazuli Ore','An ordinary lapis lazuli ore')
into items(item_name,item_description) values('Lapis Lazuli Block','A coherent lapis lazuli block')
into items(item_name,item_description) values('Dispenser','A nice dispenser')
into items(item_name,item_description) values('Sandstone','How did you even get this sandstone')
into items(item_name,item_description) values('Chiseled Sandstone','A bland chiseled sandstone')
into items(item_name,item_description) values('Smooth Sandstone','Pure smooth sandstone')
select * from dual;
/* RESPONSE STATUS:  200  */
insert into factions values ('Resistance',5,-11,-1,'This is our faction!');
/* RESPONSE STATUS:  200  */
begin join_faction('VaderVizsla','Resistance'); end;
/
/* RESPONSE STATUS:  200  */
insert into factions values ('Savage',5,14,-16,'This is our faction!');
/* RESPONSE STATUS:  200  */
begin join_faction('zuckusschewbacca','Savage'); end;
/
/* RESPONSE STATUS:  200  */
insert into factions values ('Bimyou',7,6,9,'not bad, "meh');
/* RESPONSE STATUS:  200  */
begin
join_faction('newhalen','Bimyou');
add_shop('VaderVizsla',-10,20);
add_shop('AbrahamLincoln',0,-7);
add_shop('newhalen',12,-3);
add_shop('KunSing',-13,-1);
new_message('KunSing','khalid','Hey. You: think twice --');
add_shop('zuckusschewbacca',11,-16);
new_message('zuckusschewbacca','TanoBane','Huh?');
add_shop('lionel',13,12);
add_shop('CalvinCoolidge',-2,8);
add_shop('mervyn',-17,-9);
add_shop('carmen',-18,0);
add_shop('TanoBane',17,-7);
end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('abbie',46,23);
/* RESPONSE STATUS:  200  */
begin
add_shop('abbie',8,-2);
new_message('abbie','newhalen','No. Not for money. But, if somebodyd given me half a damned excuse -- I was pretty fucked up, you know.');
add_shop('woodville',-19,-15);
add_shop('khalid',6,13);
end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('rhian',34,14);
/* RESPONSE STATUS:  200  */
begin
add_shop('rhian',-2,-9);
add_shop('LyndonBJohnson',3,-10);
add_shop('preslie',-2,-11);
add_shop('bobalando',4,-2);
add_shop('sebulbayoda',-6,-15);
add_shop('WoodrowWilson',9,-9);
add_shop('caterina',-5,-11);
add_shop('VaderVizsla',-16,1);
add_shop('AbrahamLincoln',13,1);
add_shop('newhalen',-6,3);
add_shop('KunSing',1,11);
add_shop('zuckusschewbacca',20,-12);
add_shop('lionel',5,4);
add_shop('CalvinCoolidge',-18,9);
add_shop('mervyn',-16,-14);
add_shop('carmen',-18,5);
add_shop('TanoBane',0,-9);
add_shop('abbie',18,-2);
add_shop('woodville',-17,-8);
add_shop('khalid',-8,-3);
add_shop('rhian',8,10);
add_shop('LyndonBJohnson',-16,8);
add_shop('preslie',11,-2);
add_shop('bobalando',10,16);
add_shop('sebulbayoda',-11,-16);
add_shop('WoodrowWilson',19,6);
add_shop('caterina',11,8);
add_shop('VaderVizsla',-10,15);
add_shop('newhalen',-17,5);
end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('zuckusschewbacca',28,16);
/* RESPONSE STATUS:  200  */
begin
add_shop('zuckusschewbacca',18,-7);
add_shop('lionel',-1,-13);
add_shop('CalvinCoolidge',-17,5);
add_shop('mervyn',-9,-10);
end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('carmen',43,4);
/* RESPONSE STATUS:  200  */
begin
add_shop('carmen',-15,13);
add_shop('TanoBane',9,5);
add_shop('abbie',12,13);
add_shop('woodville',-9,-5);
add_shop('khalid',10,8);
add_shop('rhian',-5,5);
add_shop('LyndonBJohnson',2,5);
add_shop('bobalando',19,18);
add_shop('sebulbayoda',-15,-6);
add_shop('WoodrowWilson',5,20);
add_shop('caterina',-9,13);
new_message('caterina','lionel','On your honor as a Roman officer, daddy?');
add_shop('AbrahamLincoln',0,12);
add_shop('KunSing',3,-13);
end;
/
/* RESPONSE STATUS:  200  */
insert all
into inventory (player_name,id_item,inv_amount) values('CalvinCoolidge',13,11)
into inventory (player_name,id_item,inv_amount) values('woodville',13,17)
select * from dual;
/* RESPONSE STATUS:  200  */
begin new_message('khalid','newhalen','Sally, so I took a few pills.  I went out dancing.  I tried to forget how upset I was about splitting up with you.  I havent lied to you.  I told you about the people Ive slept with.  I just didnt mention the few occasions I took drugs because youre so fucking judgmental I knew Id never hear the end'); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('rhian',26,16);
/* RESPONSE STATUS:  200  */
begin add_shop('preslie',-6,11); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('bobalando',48,18);
/* RESPONSE STATUS:  200  */
insert into for_sale values('bobalando',1,48,7,6);
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('newhalen',12,25);
/* RESPONSE STATUS:  200  */
insert into for_sale values('newhalen',2,12,51,2);
/* RESPONSE STATUS:  200  */
begin new_message('newhalen','carmen','Yeah, Kim told me they were giving you their Dueling Scarlets act.  Actually, theyre sophomores at Juilliard.'); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('lionel',4,29);
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('CalvinCoolidge',2,13,39,7)
into for_sale values('CalvinCoolidge',3,13,22,3)
select * from dual;
/* RESPONSE STATUS:  200  */
begin buy_items('mervyn','newhalen',2,12,2); end;
/
/* RESPONSE STATUS:  200  */
insert all
into inventory (player_name,id_item,inv_amount) values('carmen',44,13)
into inventory (player_name,id_item,inv_amount) values('khalid',9,20)
into inventory (player_name,id_item,inv_amount) values('sebulbayoda',18,27)
select * from dual;
/* RESPONSE STATUS:  200  */
begin
buy_items('sebulbayoda','CalvinCoolidge',3,13,3);
buy_items('WoodrowWilson','bobalando',1,48,1);
end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('caterina',1,18);
/* RESPONSE STATUS:  200  */
begin
new_message('AbrahamLincoln','khalid','His hatred of the Federation is apparent. He would have built a weapon of that scope for one reason. He is going after Earth.');
new_message('KunSing','CalvinCoolidge','... Im listening.');
end;
/
/* RESPONSE STATUS:  200  */
insert all
into inventory (player_name,id_item,inv_amount) values('CalvinCoolidge',1,15)
into inventory (player_name,id_item,inv_amount) values('VaderVizsla',16,7)
into inventory (player_name,id_item,inv_amount) values('AbrahamLincoln',45,17)
select * from dual;
/* RESPONSE STATUS:  200  */
begin buy_items('CalvinCoolidge','bobalando',1,48,5); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('carmen',39,14);
/* RESPONSE STATUS:  200  */
begin new_message('LyndonBJohnson','carmen','I was here yesterday.'); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('preslie',31,6);
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+6 where player_name='newhalen' and id_shop=2 and id_item=12;
/* RESPONSE STATUS:  200  */
begin buy_items('lionel','newhalen',2,12,6); end;
/
/* RESPONSE STATUS:  200  */
insert all
into inventory (player_name,id_item,inv_amount) values('mervyn',10,9)
into inventory (player_name,id_item,inv_amount) values('preslie',50,12)
into inventory (player_name,id_item,inv_amount) values('AbrahamLincoln',8,25)
select * from dual;
/* RESPONSE STATUS:  200  */
begin new_message('KunSing','CalvinCoolidge','Well, if it isnt the fabulous Baker Boys!'); end;
/
/* RESPONSE STATUS:  200  */
insert all
into inventory (player_name,id_item,inv_amount) values('CalvinCoolidge',24,22)
into inventory (player_name,id_item,inv_amount) values('VaderVizsla',18,8)
select * from dual;
/* RESPONSE STATUS:  200  */
begin new_message('zuckusschewbacca','sebulbayoda','Now put down the key --  -- and put down the address.'); end;
/
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('lionel',1,12,10,6)
into for_sale values('CalvinCoolidge',2,1,50,12)
into for_sale values('CalvinCoolidge',3,24,42,1)
into for_sale values('CalvinCoolidge',3,48,58,1)
select * from dual;
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+3 where player_name='CalvinCoolidge' and id_shop=3 and id_item=48;
/* RESPONSE STATUS:  200  */
begin
buy_items('abbie','CalvinCoolidge',3,48,2);
buy_items('abbie','CalvinCoolidge',3,48,1);
new_message('newhalen','lionel','Can you blame them?... at least the May Day parade is over.');
new_message('lionel','rhian','Theres no accounting for taste. Believe me, you could use a good kiss.  Youve spent so much time doing your duty and giving orders youve never learned how to be a woman. Its a shame, because youve got all the makings for one.  I could have helped you plenty in that department ... if youd have let go');
end;
/
/* RESPONSE STATUS:  200  */
insert all
into inventory (player_name,id_item,inv_amount) values('khalid',20,13)
into inventory (player_name,id_item,inv_amount) values('VaderVizsla',14,2)
select * from dual;
/* RESPONSE STATUS:  200  */
insert into for_sale values('VaderVizsla',2,14,48,2);
/* RESPONSE STATUS:  200  */
begin
buy_items('KunSing','CalvinCoolidge',2,13,2);
new_message('abbie','preslie','Oh, yeah.  I didnt really know my Dad...');
new_message('caterina','LyndonBJohnson','What else do you believe in?');
new_message('VaderVizsla','newhalen','Patrick? I cant hear you.');
end;
/
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('AbrahamLincoln',2,8,32,11)
into for_sale values('newhalen',1,12,37,3)
select * from dual;
/* RESPONSE STATUS:  200  */
begin buy_items('newhalen','AbrahamLincoln',2,8,4); end;
/
/* RESPONSE STATUS:  200  */
insert all
into inventory (player_name,id_item,inv_amount) values('KunSing',44,24)
into inventory (player_name,id_item,inv_amount) values('zuckusschewbacca',41,10)
select * from dual;
/* RESPONSE STATUS:  200  */
begin buy_items('carmen','lionel',1,12,5); end;
/
/* RESPONSE STATUS:  200  */
insert all
into inventory (player_name,id_item,inv_amount) values('TanoBane',49,14)
into inventory (player_name,id_item,inv_amount) values('abbie',29,6)
into inventory (player_name,id_item,inv_amount) values('woodville',39,21)
select * from dual;
/* RESPONSE STATUS:  200  */
insert into for_sale values('woodville',3,13,83,4);
/* RESPONSE STATUS:  200  */
begin
new_message('woodville','khalid','Nicky? Oh my God. Stay right there.');
buy_items('LyndonBJohnson','CalvinCoolidge',2,13,3);
buy_items('LyndonBJohnson','CalvinCoolidge',2,1,7);
end;
/
/* RESPONSE STATUS:  200  */
insert into for_sale values('LyndonBJohnson',2,1,90,3);
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+3 where player_name='LyndonBJohnson' and id_shop=2 and id_item=1;
/* RESPONSE STATUS:  200  */
begin
buy_items('preslie','CalvinCoolidge',3,48,1);
buy_items('preslie','CalvinCoolidge',3,24,1);
buy_items('preslie','VaderVizsla',2,14,1);
buy_items('WoodrowWilson','woodville',3,13,1);
buy_items('caterina','VaderVizsla',2,14,1);
end;
/
/* RESPONSE STATUS:  200  */
insert into for_sale values('lionel',1,4,98,6);
/* RESPONSE STATUS:  200  */
begin buy_items('CalvinCoolidge','woodville',3,13,1); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('carmen',10,20);
/* RESPONSE STATUS:  200  */
begin
buy_items('woodville','CalvinCoolidge',2,13,1);
buy_items('woodville','LyndonBJohnson',2,1,4);
end;
/
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('rhian',3,26,72,1)
into for_sale values('sebulbayoda',3,13,72,2)
select * from dual;
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+1 where player_name='sebulbayoda' and id_shop=3 and id_item=13;
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('WoodrowWilson',43,28);
/* RESPONSE STATUS:  200  */
begin
buy_items('WoodrowWilson','sebulbayoda',3,13,2);
buy_items('caterina','sebulbayoda',3,13,1);
end;
/
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('WoodrowWilson','VaderVizsla');
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('lionel',27,21);
/* RESPONSE STATUS:  200  */
begin join_faction('CalvinCoolidge','Savage'); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('carmen',51,10);
/* RESPONSE STATUS:  200  */
begin buy_items('TanoBane','LyndonBJohnson',2,1,2); end;
/
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('rhian',1,34,10,13)
into for_sale values('rhian',1,26,35,15)
select * from dual;
/* RESPONSE STATUS:  200  */
begin buy_items('LyndonBJohnson','AbrahamLincoln',2,8,2); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('KunSing',22,18);
/* RESPONSE STATUS:  200  */
begin
buy_items('mervyn','lionel',1,4,2);
buy_items('mervyn','lionel',1,4,1);
buy_items('abbie','rhian',3,26,1);
end;
/
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('woodville',1,1,15,2)
into for_sale values('woodville',1,13,12,3)
select * from dual;
/* RESPONSE STATUS:  200  */
begin
buy_items('sebulbayoda','woodville',3,13,2);
buy_items('caterina','rhian',1,34,1);
end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('CalvinCoolidge',31,14);
/* RESPONSE STATUS:  200  */
begin
buy_items('mervyn','newhalen',1,12,1);
buy_items('mervyn','AbrahamLincoln',2,8,2);
end;
/
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('caterina','sebulbayoda');
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('WoodrowWilson',3,13,75,1)
into for_sale values('WoodrowWilson',3,43,92,4)
select * from dual;
/* RESPONSE STATUS:  200  */
begin
new_message('WoodrowWilson','khalid','Young? Shes fuckin nine-years-old, same age as Lovejoys kid. Bernie. One she calls Bernard. Have you read the script?');
buy_items('newhalen','lionel',1,4,1);
buy_items('lionel','rhian',1,34,11);
end;
/
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('lionel','mervyn');
/* RESPONSE STATUS:  200  */
begin
buy_items('khalid','AbrahamLincoln',2,8,3);
buy_items('LyndonBJohnson','WoodrowWilson',3,13,1);
end;
/
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+1 where player_name='bobalando' and id_shop=1 and id_item=48;
/* RESPONSE STATUS:  200  */
insert all
into inventory (player_name,id_item,inv_amount) values('WoodrowWilson',45,24)
into inventory (player_name,id_item,inv_amount) values('newhalen',45,10)
select * from dual;
/* RESPONSE STATUS:  200  */
begin
buy_items('lionel','WoodrowWilson',3,43,4);
join_faction('lionel','Resistance');
end;
/
/* RESPONSE STATUS:  200  */
insert all
into kills(waskilled_name,killed_name) values('CalvinCoolidge','carmen')
into kills(waskilled_name,killed_name) values('bobalando','TanoBane')
select * from dual;
/* RESPONSE STATUS:  200  */
begin
buy_items('TanoBane','bobalando',1,48,1);
new_message('abbie','preslie','Why?');
end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('rhian',48,10);
/* RESPONSE STATUS:  200  */
begin buy_items('LyndonBJohnson','lionel',1,12,1); end;
/
/* RESPONSE STATUS:  200  */
update inventory set inv_amount=inv_amount+39 where player_name='carmen' and id_item=39;
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('TanoBane',25,17);
/* RESPONSE STATUS:  200  */
begin buy_items('TanoBane','lionel',1,4,1); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('abbie',53,11);
/* RESPONSE STATUS:  200  */
begin buy_items('khalid','newhalen',1,12,1); end;
/
/* RESPONSE STATUS:  200  */
insert all
into kills(waskilled_name,killed_name) values('sebulbayoda','preslie')
into kills(waskilled_name,killed_name) values('preslie','sebulbayoda')
select * from dual;
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('WoodrowWilson',35,16);
/* RESPONSE STATUS:  200  */
begin buy_items('lionel','CalvinCoolidge',2,13,1); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('CalvinCoolidge',11,15);
/* RESPONSE STATUS:  200  */
begin new_message('CalvinCoolidge','preslie','Sorry.  I dont feel like sitting still today.'); end;
/
/* RESPONSE STATUS:  200  */
insert all
into inventory (player_name,id_item,inv_amount) values('abbie',12,21)
into inventory (player_name,id_item,inv_amount) values('LyndonBJohnson',4,21)
select * from dual;
/* RESPONSE STATUS:  200  */
begin buy_items('WoodrowWilson','lionel',1,4,1); end;
/
/* RESPONSE STATUS:  200  */
update inventory set inv_amount=inv_amount+10 where player_name='CalvinCoolidge' and id_item=13;
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('AbrahamLincoln','rhian');
/* RESPONSE STATUS:  200  */
insert into for_sale values('preslie',1,14,97,1);
/* RESPONSE STATUS:  200  */
begin
buy_items('preslie','rhian',1,34,1);
buy_items('preslie','rhian',1,26,9);
buy_items('bobalando','preslie',1,14,1);
buy_items('bobalando','rhian',1,26,4);
end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('WoodrowWilson',25,6);
/* RESPONSE STATUS:  200  */
begin
new_message('AbrahamLincoln','woodville','Why is that?');
new_message('carmen','bobalando','Your mother.');
join_faction('rhian','Savage');
new_message('newhalen','lionel','Yes. They want to help.');
end;
/
/* RESPONSE STATUS:  200  */
insert all
into inventory (player_name,id_item,inv_amount) values('KunSing',26,24)
into inventory (player_name,id_item,inv_amount) values('CalvinCoolidge',53,28)
select * from dual;
/* RESPONSE STATUS:  200  */
begin
buy_items('CalvinCoolidge','newhalen',1,12,1);
buy_items('abbie','rhian',1,26,2);
end;
/
/* RESPONSE STATUS:  200  */
insert into for_sale values('khalid',3,9,35,17);
/* RESPONSE STATUS:  200  */
begin new_message('rhian','WoodrowWilson','Bad. Sent to the City Hospital. They ruptured his hernia again.'); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('preslie',43,25);
/* RESPONSE STATUS:  200  */
begin buy_items('sebulbayoda','khalid',3,9,4); end;
/
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('woodville','WoodrowWilson');
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('VaderVizsla',50,26);
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('rhian','VaderVizsla');
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('lionel',1,6);
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('VaderVizsla','TanoBane');
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('khalid',2,8,53,3)
into for_sale values('khalid',2,12,36,1)
into for_sale values('khalid',2,9,21,1)
into for_sale values('khalid',2,20,62,10)
into for_sale values('rhian',2,48,67,1)
select * from dual;
/* RESPONSE STATUS:  200  */
begin
buy_items('rhian','khalid',3,9,5);
new_message('rhian','WoodrowWilson','Go ahead.');
new_message('preslie','abbie','Oh, or certainly by this evening, yes? The evenings a great time, isnt it, Alex boy?');
buy_items('caterina','rhian',2,48,1);
buy_items('newhalen','woodville',1,1,2);
buy_items('newhalen','woodville',1,13,1);
end;
/
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('lionel',2,43,7,4)
into for_sale values('lionel',2,4,95,12)
select * from dual;
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('caterina','carmen');
/* RESPONSE STATUS:  200  */
begin
buy_items('LyndonBJohnson','lionel',2,43,4);
buy_items('LyndonBJohnson','lionel',2,4,4);
join_faction('LyndonBJohnson','Resistance');
new_message('sebulbayoda','WoodrowWilson','Are you all right, Dorothy?');
end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('AbrahamLincoln',26,26);
/* RESPONSE STATUS:  200  */
begin buy_items('newhalen','woodville',1,13,2); end;
/
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('lionel',2,34,97,7)
into for_sale values('lionel',2,13,98,1)
into for_sale values('lionel',2,27,10,18)
select * from dual;
/* RESPONSE STATUS:  200  */
begin new_message('lionel','newhalen','You know what I mean. Leave her alone.'); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('mervyn',21,4);
/* RESPONSE STATUS:  200  */
begin
buy_items('carmen','khalid',3,9,7);
buy_items('rhian','CalvinCoolidge',2,1,5);
buy_items('preslie','lionel',2,13,1);
buy_items('preslie','lionel',2,27,2);
end;
/
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('preslie',2,26,11,1)
into for_sale values('preslie',2,27,55,1)
into for_sale values('preslie',2,34,5,1)
select * from dual;
/* RESPONSE STATUS:  200  */
begin
buy_items('sebulbayoda','lionel',2,34,3);
buy_items('KunSing','preslie',2,26,1);
buy_items('KunSing','preslie',2,27,1);
end;
/
/* RESPONSE STATUS:  200  */
update inventory set inv_amount=inv_amount+19 where player_name='abbie' and id_item=26;
/* RESPONSE STATUS:  200  */
insert all
into inventory (player_name,id_item,inv_amount) values('woodville',10,9)
into inventory (player_name,id_item,inv_amount) values('AbrahamLincoln',16,29)
into inventory (player_name,id_item,inv_amount) values('carmen',36,6)
select * from dual;
/* RESPONSE STATUS:  200  */
insert all
into kills(waskilled_name,killed_name) values('LyndonBJohnson','carmen')
into kills(waskilled_name,killed_name) values('carmen','woodville')
select * from dual;
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('rhian',33,19);
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('mervyn','sebulbayoda');
/* RESPONSE STATUS:  200  */
begin
new_message('mervyn','bobalando','Where is my family?');
buy_items('woodville','khalid',2,9,1);
buy_items('woodville','khalid',2,12,1);
buy_items('woodville','khalid',2,20,7);
end;
/
/* RESPONSE STATUS:  200  */
insert all
into inventory (player_name,id_item,inv_amount) values('LyndonBJohnson',45,18)
into inventory (player_name,id_item,inv_amount) values('sebulbayoda',53,16)
select * from dual;
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('caterina',3,48,94,1)
into for_sale values('caterina',3,13,19,1)
select * from dual;
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('KunSing',20,8);
/* RESPONSE STATUS:  200  */
begin
buy_items('KunSing','lionel',2,34,1);
buy_items('KunSing','lionel',2,34,2);
new_message('abbie','KunSing','We were worried about you guys so we left early to see if you were --');
end;
/
/* RESPONSE STATUS:  200  */
update inventory set inv_amount=inv_amount+28 where player_name='woodville' and id_item=12;
/* RESPONSE STATUS:  200  */
begin join_faction('khalid','Resistance'); end;
/
/* RESPONSE STATUS:  200  */
update inventory set inv_amount=inv_amount+7 where player_name='preslie' and id_item=34;
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('bobalando',36,26);
/* RESPONSE STATUS:  200  */
begin
buy_items('newhalen','khalid',3,9,1);
new_message('carmen','bobalando','Since I was a kid.  My mom wanted a girl, so she used to dress me in girlie clothing.  It just kinda became a habit.');
end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('abbie',24,21);
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('LyndonBJohnson',2,45,76,8)
into for_sale values('preslie',1,43,71,5)
select * from dual;
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+12 where player_name='preslie' and id_shop=1 and id_item=43;
/* RESPONSE STATUS:  200  */
insert into for_sale values('preslie',1,34,55,3);
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('WoodrowWilson','preslie');
/* RESPONSE STATUS:  200  */
begin buy_items('sebulbayoda','lionel',2,27,5); end;
/
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('KunSing','WoodrowWilson');
/* RESPONSE STATUS:  200  */
begin
buy_items('VaderVizsla','khalid',2,8,3);
new_message('mervyn','CalvinCoolidge','You dont kill anyone.');
end;
/
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('TanoBane',3,48,27,1)
into for_sale values('TanoBane',3,49,39,6)
into for_sale values('TanoBane',3,4,56,1)
into for_sale values('rhian',1,1,93,1)
select * from dual;
/* RESPONSE STATUS:  200  */
begin new_message('rhian','WoodrowWilson','What do you think?'); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('LyndonBJohnson',52,23);
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('AbrahamLincoln','LyndonBJohnson');
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('sebulbayoda',47,14);
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('KunSing',3,27,80,1)
into for_sale values('KunSing',3,13,82,2)
into for_sale values('KunSing',3,26,49,11)
into for_sale values('KunSing',3,44,37,16)
select * from dual;
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('zuckusschewbacca',16,14);
/* RESPONSE STATUS:  200  */
begin
new_message('CalvinCoolidge','sebulbayoda','Thats not crazy. I like you too.');
buy_items('abbie','lionel',2,27,9);
buy_items('abbie','lionel',2,27,1);
buy_items('abbie','lionel',2,27,1);
buy_items('abbie','TanoBane',3,48,1);
new_message('rhian','WoodrowWilson','Art. Well what do you want to know about it.');
end;
/
/* RESPONSE STATUS:  200  */
insert into for_sale values('LyndonBJohnson',2,43,77,4);
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+8 where player_name='LyndonBJohnson' and id_shop=2 and id_item=45;
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+2 where player_name='LyndonBJohnson' and id_shop=2 and id_item=45;
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('LyndonBJohnson',2,8,57,2)
into for_sale values('preslie',3,43,47,6)
into for_sale values('preslie',3,34,26,1)
select * from dual;
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('bobalando',16,27);
/* RESPONSE STATUS:  200  */
begin
buy_items('bobalando','preslie',2,34,1);
buy_items('newhalen','rhian',1,1,1);
end;
/
/* RESPONSE STATUS:  200  */
update inventory set inv_amount=inv_amount+25 where player_name='KunSing' and id_item=44;
/* RESPONSE STATUS:  200  */
insert into for_sale values('zuckusschewbacca',1,16,32,4);
/* RESPONSE STATUS:  200  */
update inventory set inv_amount=inv_amount+18 where player_name='lionel' and id_item=34;
/* RESPONSE STATUS:  200  */
begin new_message('CalvinCoolidge','AbrahamLincoln','Not --'); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('carmen',11,24);
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('lionel','woodville');
/* RESPONSE STATUS:  200  */
begin
buy_items('WoodrowWilson','preslie',1,43,6);
buy_items('WoodrowWilson','preslie',1,34,2);
buy_items('WoodrowWilson','preslie',1,43,1);
end;
/
/* RESPONSE STATUS:  200  */
insert into players(name) values('charley');
/* RESPONSE STATUS:  200  */
begin buy_items('AbrahamLincoln','khalid',2,20,3); end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('newhalen',48,21);
/* RESPONSE STATUS:  200  */
begin
buy_items('zuckusschewbacca','lionel',2,34,1);
buy_items('lionel','KunSing',3,13,2);
buy_items('lionel','KunSing',3,27,1);
new_message('carmen','LyndonBJohnson','De Vries?');
end;
/
/* RESPONSE STATUS:  200  */
update inventory set inv_amount=inv_amount+24 where player_name='woodville' and id_item=13;
/* RESPONSE STATUS:  200  */
begin buy_items('khalid','KunSing',3,26,6); end;
/
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('TanoBane','preslie');
/* RESPONSE STATUS:  200  */
begin
new_message('sebulbayoda','abbie','Im not good at lying.');
add_shop('charley',17,-2);
end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('VaderVizsla',43,15);
/* RESPONSE STATUS:  200  */
begin
buy_items('newhalen','LyndonBJohnson',2,45,7);
buy_items('newhalen','LyndonBJohnson',2,8,1);
buy_items('lionel','LyndonBJohnson',2,45,7);
buy_items('lionel','LyndonBJohnson',2,8,1);
buy_items('CalvinCoolidge','zuckusschewbacca',1,16,2);
end;
/
/* RESPONSE STATUS:  200  */
insert into for_sale values('mervyn',2,10,55,7);
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('TanoBane',53,14);
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('zuckusschewbacca','abbie');
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('abbie',1,27,85,4)
into for_sale values('abbie',1,26,42,10)
into for_sale values('abbie',1,24,24,11)
into for_sale values('abbie',1,29,25,5)
into for_sale values('preslie',2,24,30,1)
select * from dual;
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+1 where player_name='preslie' and id_shop=2 and id_item=27;
/* RESPONSE STATUS:  200  */
begin
join_faction('preslie','Resistance');
add_shop('charley',2,-17);
buy_items('VaderVizsla','preslie',2,24,1);
buy_items('VaderVizsla','preslie',2,27,1);
end;
/
/* RESPONSE STATUS:  200  */
insert into for_sale values('AbrahamLincoln',3,26,53,20);
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+5 where player_name='AbrahamLincoln' and id_shop=3 and id_item=26;
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('AbrahamLincoln',3,16,98,2)
into for_sale values('AbrahamLincoln',3,8,88,1)
into for_sale values('AbrahamLincoln',3,20,11,3)
select * from dual;
/* RESPONSE STATUS:  200  */
begin
buy_items('KunSing','TanoBane',3,4,1);
buy_items('KunSing','TanoBane',3,49,3);
end;
/
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('preslie','KunSing');
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('TanoBane',1,1,10,2)
into for_sale values('TanoBane',1,53,14,1)
into for_sale values('TanoBane',1,25,85,7)
select * from dual;
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+2 where player_name='TanoBane' and id_shop=1 and id_item=25;
/* RESPONSE STATUS:  200  */
insert into for_sale values('TanoBane',1,49,85,2);
/* RESPONSE STATUS:  200  */
begin buy_items('abbie','zuckusschewbacca',1,16,1); end;
/
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+1 where player_name='woodville' and id_shop=1 and id_item=1;
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('woodville',1,10,67,8)
into for_sale values('woodville',1,20,95,7)
select * from dual;
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+1 where player_name='khalid' and id_shop=2 and id_item=20;
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+2 where player_name='khalid' and id_shop=2 and id_item=9;
/* RESPONSE STATUS:  200  */
insert into for_sale values('khalid',2,26,42,5);
/* RESPONSE STATUS:  200  */
begin
new_message('khalid','KunSing','Whats wrong with you?');
buy_items('bobalando','khalid',2,26,2);
buy_items('bobalando','khalid',2,9,1);
buy_items('caterina','TanoBane',1,53,1);
buy_items('caterina','TanoBane',1,1,1);
buy_items('caterina','TanoBane',1,49,2);
buy_items('caterina','TanoBane',1,1,1);
end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('charley',16,4);
/* RESPONSE STATUS:  200  */
begin
add_shop('charley',18,-11);
buy_items('VaderVizsla','TanoBane',3,49,2);
buy_items('KunSing','abbie',1,26,4);
buy_items('KunSing','abbie',1,24,6);
join_faction('KunSing','Resistance');
buy_items('zuckusschewbacca','caterina',3,48,1);
buy_items('carmen','zuckusschewbacca',1,16,1);
end;
/
/* RESPONSE STATUS:  200  */
update inventory set inv_amount=inv_amount+9 where player_name='abbie' and id_item=16;
/* RESPONSE STATUS:  200  */
begin join_faction('abbie','Savage'); end;
/
/* RESPONSE STATUS:  200  */
insert into for_sale values('woodville',2,13,83,5);
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+8 where player_name='woodville' and id_shop=2 and id_item=13;
/* RESPONSE STATUS:  200  */
begin buy_items('rhian','woodville',2,13,7); end;
/
/* RESPONSE STATUS:  200  */
update inventory set inv_amount=inv_amount+22 where player_name='LyndonBJohnson' and id_item=45;
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('newhalen','carmen');
/* RESPONSE STATUS:  200  */
begin
buy_items('carmen','preslie',1,43,2);
new_message('TanoBane','KunSing','My wife wears a seven.  You dont look like a seven to me.');
buy_items('woodville','preslie',3,34,1);
buy_items('woodville','AbrahamLincoln',3,16,1);
buy_items('woodville','AbrahamLincoln',3,8,1);
join_faction('woodville','Savage');
end;
/
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('khalid',39,21);
/* RESPONSE STATUS:  200  */
begin
buy_items('khalid','KunSing',3,44,3);
buy_items('rhian','KunSing',3,26,1);
end;
/
/* RESPONSE STATUS:  200  */
insert into for_sale values('preslie',3,26,61,8);
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+2 where player_name='preslie' and id_shop=3 and id_item=43;
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('preslie',3,31,87,4)
into for_sale values('bobalando',2,36,97,11)
into for_sale values('bobalando',2,9,35,1)
select * from dual;
/* RESPONSE STATUS:  200  */
begin
buy_items('VaderVizsla','woodville',2,13,3);
buy_items('lionel','TanoBane',1,25,3);
buy_items('carmen','abbie',1,24,1);
buy_items('abbie','KunSing',3,26,3);
buy_items('woodville','abbie',1,29,2);
buy_items('woodville','abbie',1,26,3);
buy_items('khalid','preslie',1,43,2);
buy_items('khalid','preslie',1,34,1);
end;
/
/* RESPONSE STATUS:  200  */
insert into kills(waskilled_name,killed_name) values('woodville','LyndonBJohnson');
/* RESPONSE STATUS:  200  */
update for_sale set sale_amount=sale_amount+1 where player_name='bobalando' and id_shop=2 and id_item=36;
/* RESPONSE STATUS:  200  */
insert all
into for_sale values('bobalando',2,16,96,16)
into for_sale values('bobalando',2,48,61,11)
select * from dual;
/* RESPONSE STATUS:  200  */
insert into players(name) values('randall');
/* RESPONSE STATUS:  200  */
insert into inventory (player_name,id_item,inv_amount) values('zuckusschewbacca',13,22);
/* RESPONSE STATUS:  200  */

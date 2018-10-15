import random
candidates = ["Deborah Looney","Verna Montalvo","Sara Shelby","Jennifer Miller Land","Linda Vickrey Aldredge","Marie Gaunce","Pamela Clore","Dorene Branum","Alice Neuville","Wadette Matthews","Barbara Kindsfather",
         "Benalee Allen," "Neli Masuma","Monica Stennis","Dot Elam","Ann Haines","James Sisouvanh Soumphonphakdy","Monín Torres Vargas","Lourdes Moore","Cindy Edwards","Debra Bigham","Maureen Sadowski",
         "Viola Rojas","Joy  Green","Linda Brunson","Karen Klein","Peggy Spann Collins","Dell Dimarco","Angie Wilburn","Sandra Vickrey Spence","Leslie Wagner","Barbie Siewers","Yvette Davis Frederick","Ana Cervantes",
         "Linda Clark" "Sherry Jones","DeLische Wall Ferguson","Myrna McKelvy Wing","Adrienne Jarrett","Allison Arnold","Linda Kay Vaughn Mcpike","Michelle Gleason","Carmen Luisa Vazquez","Lea Ann Bray-Salinas","Tracey Haberle Marino",
         "Charlotte Yeager","Ashley McNesby","Patricia Coburn","Debbie Litton Williams","Aymie Thornton","Bill Laney","Jo R Rohal","Liz Cambra","Diana Day Burks","Mary Helen Curl","Deborah Brewer Cook","Lorie A Gassert",
         "Lanita Lynn Battle-Matthews","Michelle Smith Reyna", "Kristen Terrell", "Becky Campbell", "Stephanie Rotthaus", "Jeannie Vanderburg", "Nora Macias", "Denise Brown", "Cindy Smrt", "Carolyn Alexander",
         "Theresa Hollingsworth","Deborah Looney"]
winner = random.randint(0, len(candidates) -1)
print(f"Congratulations to our winner...{candidates[winner]}")

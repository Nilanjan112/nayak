<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Lock - Read More</title>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="index.php">Home</a></li>
                <li><a href="gallery.php">Gallery</a></li>
                <li><a href="artists.php">Artists</a></li>
                <li><a href="shop.php">Shop</a></li>
                <li><a href="news.php">News</a></li>
                <li><a href="contact.php">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <h1>John Doe Showcase</h1>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non risus. Suspendisse lectus tortor, dignissim sit amet, adipiscing nec, ultricies sed, dolor. Cras elementum ultrices diam. Maecenas ligula eros, blandit nec, pulvinar at, mollis ac, nulla. Curabitur auctor semper nulla. Donec varius orci eget risus. Duis nibh mi, congue eu, accumsan eleifend, sagittis quis, diam. Duis eget orci sit amet orci dignissim rutrum. </p>
    </main>

    <footer>
        <p>Copyright © 2023 The Lock</p>
    </footer>
</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Lock - [Page Title]</title>
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="index.php">Home</a></li>
                <li><a href="gallery.php">G
                    <?php echo $_GET['id']; ?>
                </a></li>
            </ul>
        </nav>
    </header>

    <main>
        <img src="<?php echo "images/".$_GET['id'].".jpg";?>" alt="" />
        
        <h2>Title: <?php echo $image_data[0]['title']; ?></h2>
        <h4>Date: <?php echo $image_data[0]['date']; ?></h4>
        <p>Description: <?php echo nl2br($image_data[0]['description']); ?></p>
    </main>
    
    <form action="comment_add.php?id=<?php echo $_GET['id']; ?>" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required />
        <label for="email">Email (optional):</label>
        <input type="email" id="email" name="email" />
        <label for="website">Website (optional):</label>
        <input type="url" id="website" name="website" />
        <label for="content">Comment:</label>
        <textarea id="content" name="content" rows="6" cols="50" required ></textarea>
        <button type="submit">Submit Comment</button>
    </form> 

    <section>   
        
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define o = Character("Oldman")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    "เมื่อ 16 ปีก่อนมีคนกล่าวไว้ว่า" 
    "องค์รัชทายาทของท่านราชาผู้ปกครองแห่งอาณาจักร \"อัลราเซีย\" จะเป็นคนที่โค่นพระองค์และขึ้นครองราชย์แทน"
    "แต่มีรึที่องค์ราชาจะอยู่นิ่งดูดาย" 
    "ถึงแม้สิ่งที่ท่านราชาจะทำต่อจากที่การกำเนิดขององค์รัชทายาทนั้นมันจะฟังดูโหดร้าย แต่ถ้ามันทำให้เขาได้ปกครองอาณาจักรแห่งนี้ต่อเขาก็ยอมทำทุกอย่าง"
    "แม้ต้องจัดการโอรสของตนเอง แต่ก็มิรู้ว่ามันใช่ความจริงหรือไม่" 
    "เพราะมันก็เป็นแค่คำพูดปากต่อปากของคนรับใช้ภายในวังหลวง"
    
    scene oldman_cabin with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "เห้อ~ ท่านปู่ไม่มีเรื่องเล่าเรื่องอื่นแล้วรึไง ถึงได้เล่าแต่เรื่องเดิมๆให้ข้าฟัง" 
    "เสียงใสของหนุ่มน้อยพูดกับปู่ของตัวเองด้วยน้ำเสียงที่ดูจะไม่พอใจเล็กน้อย บรรยากาศภายในห้องเงียบไป"
    
    # This ends the game.

    return

add_library('ImageLoader')
add_library('sound')




def setup():
    global sf,x, y
    size(600,600)
    x = 0
    y = 0

    sf = SoundFile(this, "lotus.wav")    
    sf.play()
    sf.loop(1)
    print("Orange")
    frameRate(7)

    

    
def draw():
    global sf, x, y
    img = loadImage("palm.gif")
    image(img, 0, 0)

    
    #Pong Text
    fill(random(190,255),random(190,255),random(190,255))
    
    myFont = createFont("retro.ttf", 32)
    textFont(myFont)
    textAlign(CENTER, CENTER)
    textSize(100) 
    sss = "Pong"
    text(sss, width/2, height/ 6)
    
    #Rectangles
    fill(255)
    noStroke()
    rect(100, 300, 155, 55, 100)
    rect(345, 300, 155, 55, 100)
    
    fill(255,0,0)
    textSize(20)
    text("Start", 180, 322)
    text("Exit", 425, 322,)
    
    # print("Mouse x:", mouseX)
    # print("Mouse y:", mouseY)

def mousePressed():
    global sf, x ,y

   
    
def mouseClicked():
    global sf, x, y
    
    if mouseX > 100 and mouseX < 255 and mouseY > 300 and mouseY < 355:
        print("True 1")
    elif mouseX > 345 and mouseX < 500 and mouseY > 300 and mouseY < 355:
        print("True 2")
    else:
        print("False")
    
    
    
    

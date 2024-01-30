import kivy 
    
from kivy.app import App 
    
from kivy.uix.button import Button
  
kivy.require('1.9.0')   


#our class to create a button and execute it
class ButtonApp(App): 
        
    def build(self): 
  
        # create an image a button 
        # Adding images back1.png image as button
        # Adding image back2.png as the background when clicked
        testBtn = Button(text ="Hello World !",
                    background_normal = 'back1.png',
                    background_down ='back2.png'
                  ) 
      
        return testBtn 
            
    
# binding ButtonApp to a root
root = ButtonApp() 
    
root.run()

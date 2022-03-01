.model small
.stack
.data
   msg1 db "Hola mundo!", "$"
 
.code
 
.startup               
   mov ah, 09h
   mov dx, offset msg1
   int 21h

   mov ah, 01h
   int 21h

   mov ah, 4ch
   int 21h
end             
.exit
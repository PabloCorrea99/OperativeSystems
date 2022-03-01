.model Small
.stack
.data
   msg2 db 10,13, "Ingrese el mensaje: $"
   msg3 db 10,13, "El mensaje es: $"
.code 
.startup  

   mov ah, 09h
   mov dx, offset msg2
   int 21h

   mov dl, al

   mov ah, 01h
   int 21h

   mov ah,09h
   mov dx, offset msg3
   int 21h

   mov dl, al

   mov ah, 02h
   int 21h

   mov ah, 4ch
   int 21h
 
end
.exit
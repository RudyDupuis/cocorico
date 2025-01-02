section .text
global _start
_start:
mov qword [nom], str_0
mov qword [nom], str_1
mov rsi, [nom]
mov rdx, 1000
mov rax, 1
mov rdi, 1
syscall
mov rax, 60
xor rdi, rdi
syscall

section .data
nom dq 0
str_0 db "ma phrase à afficher", 0
str_1 db "au final je veux afficher çà", 0
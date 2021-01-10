n1=float(input())
n2=float(input())
n3=float(input())
frequencia=float(input())
frequenciaMinima=frequencia*100
media_ponderada=round((n1*2+n2*2+n3*3)/(7),1)

print('Frequencia: {:.0f}%'.format(frequenciaMinima))
print('Media:',media_ponderada)

if frequenciaMinima<75:
    print('Aluno reprovado por faltas!')
else:          
    if media_ponderada>9.0:
        print('Aluno aprovado com louvor!')
    elif media_ponderada>=6.0:
        print('Aluno aprovado!')
    elif media_ponderada>=4.0:
        print('Aluno de rec!')
    else: 
        print('Aluno reprovado!')
    
    

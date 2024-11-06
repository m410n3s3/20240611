# # def CriaMatriz(NumLinhas, NumColunas): 
# # 	matrizA = [None]*NumLinhas
# # 	for i in range(NumLinhas): 
# # 		matrizA[i] = [None]*NumColunas
# # 	return matrizA

# # def ImprimirMatriz(M): 
# # 	NumLinhas = len(M)
# # 	NumColunas = len(M[0])
# # 	for i in range(NumLinhas): 
# # 		for j in range(NumColunas): 
# # 			print(M[i][j], end = " ")
# # 		print()	

# # def PreencheMatrizPorLinhas(M): 
# # 	NumLinhas = len(M)
# # 	NumColunas = len(M[0])
# # 	print("NumLinhas = ", NumLinhas)
# # 	for i in range(NumLinhas): 
# # 		for j in range(NumColunas): 
# # 			M[i][j]=i*NumColunas+j+1
# # 	ImprimirMatriz(M)
# # 	return M		

	
# def CriaMatriz(NumLinhas, NumColunas): 
# 	matrizA = [None]*NumLinhas
# 	for i in range(NumLinhas): 
# 		matrizA[i] = [None]*NumColunas
# 	return matrizA

# def EhMatriz(M):
# 	if type(M) == list:
# 	    nlinhas = len(M)
#         if type(M[0]) == list:
#             ncols = len(M[0])
#             return nlinhas, ncols
#         else:
#             print("Vetor de 1 dimensao")
#             return False
#     else:
#         print("Entada não é vetor")
#         return False

# def ImprimirMatriz(M): 
# 	NumLinhas = len(M)
# 	NumColunas = len(M[0])
# 	for i in range(NumLinhas): 
# 		for j in range(NumColunas): 
# 			print(M[i][j], end = " ")
# 		print()	

# def PreencheMatrizPorColunas(M): 
# 	VerificaMatriz = EhMatriz(M)
# 	if (VerificaMatriz != False):
# 		NumLinhas, NumColunas

	

# if __name__ == "__main__": 
# 	#A=CriaMatriz(4,3)			
# 	#PreencheMatrizPorLinhas(A)

# 	A=CriaMatriz(4,3)			
# 	PreencheMatrizPorColunas(A)


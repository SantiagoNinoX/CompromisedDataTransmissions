# E1: Transmisiones de Datos Comprometidas.
# Autores: Santiago Ramírez Niño (A01665906),
# Alejandro Ignacio Vargas Cruz (A01659714) y
# Omar Llano Tostado (A01660505).
# Materia: Análisis de Algoritmos Avanzados.
# Profesor: Dr. Salvador E. Venegas-Andraca.
# Fecha de entrega: 06 de noviembre de 2025.

#Algoritmo KMP para encontrar patrones en cadenas de texto. Complejidad O(n + m).
def kmp(text, pattern):
    n = len(text)          # Longitud del texto
    m = len(pattern)       # Longitud del patrón

    # Preprocesamiento del patrón para crear el array de fallos (lps)
    lps = [0] * m
    j = 0  # longitud del prefijo anterior
    i = 1

    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                lps[i] = 0
                i += 1

    # Búsqueda del patrón en el texto usando el array lps
    i = 0  # índice para text
    j = 0  # índice para pattern
    occurrences = []

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == m:
            occurrences.append(i - j)  # Patrón encontrado, guardar la posición
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    #Regresar true si se encontró el patrón (booleano si el arreglo de ocurrencias no está vacío) y las posiciones donde se encontró
    return len(occurrences) > 0

# Funcion para encontrar palindromos con Manacher. Complejidad O(n).
def manacher(S):
    # Preprocesar la cadena
    T = '#' + '#'.join(S) + '#'   # Insertar separadores
    n = len(T)    # Longitud de la cadena transformada
    P = [0] * n     # Array para almacenar la longitud del palíndromo en cada centro
    C = 0   # Centro del palíndromo más a la derecha
    R = 0       # Borde derecho del palíndromo más a la derecha

    for i in range(n):       # Iterar sobre cada carácter en T
        mirror = 2 * C - i        # Índice espejo de i con respecto a C

        if i < R:        # Si i está dentro del borde derecho R, usar el valor espejo 
            P[i] = min(R - i, P[mirror])

        # Intentar expandir el palíndromo centrado en i
        while (i + P[i] + 1 < n and i - P[i] - 1 >= 0) and (T[i + P[i] + 1] == T[i - P[i] - 1]):
            P[i] += 1         # Expandir el radio del palíndromo mientras los caracteres coincidan

        # Si se expandió más allá del borde actual, actualizar C y R
        if i + P[i] > R:      
            C = i
            R = i + P[i]

    # Encontrar el índice con el palíndromo más largo
    max_len = max(P)     
    center_index = P.index(max_len)      
    start = (center_index - max_len) // 2
    return S[start:start + max_len]    # Extraer la subcadena palíndroma más larga de S

# Funcion para leer archivos y ejecutar las funciones anteriores
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

# Funcion para encontrar el Largest Common Substring entre dos transmisiones. 
def lcs(s1, s2):
    #Longest Common Substring usando Binary Search + Rolling Hash.
    #Complejidad: O(n log n) tiempo, O(n) memoria.
    n1, n2 = len(s1), len(s2)
    
    if n1 == 0 or n2 == 0:
        return 1, 0
    
    def get_hashes(s, length):
        if length == 0:
            return {}
        
        hashes = {}
        base = 256
        mod = 10**9 + 7
        
        # Hash inicial
        h = 0
        power = 1
        for i in range(length):
            h = (h * base + ord(s[i])) % mod
            if i < length - 1:
                power = (power * base) % mod
        
        hashes[h] = [0]
        
        # Rolling hash
        for i in range(1, len(s) - length + 1):
            h = (h - ord(s[i - 1]) * power) % mod
            h = (h * base + ord(s[i + length - 1])) % mod
            h = (h + mod) % mod
            
            if h not in hashes:
                hashes[h] = []
            hashes[h].append(i)
        
        return hashes
    
    def check_length(length):
        hashes1 = get_hashes(s1, length)
        hashes2 = get_hashes(s2, length)
        
        for h in hashes1:
            if h in hashes2:
                for pos1 in hashes1[h]:
                    for pos2 in hashes2[h]:
                        if s1[pos1:pos1 + length] == s2[pos2:pos2 + length]:
                            return True, pos1
        
        return False, -1
    
    # Búsqueda binaria
    left, right = 0, min(n1, n2)
    best_length = 0
    best_pos = 0
    
    while left <= right:
        mid = (left + right) // 2
        found, pos = check_length(mid)
        
        if found:
            best_length = mid
            best_pos = pos
            left = mid + 1
        else:
            right = mid - 1
    
    if best_length == 0:
        return 1, 0
    
    return best_pos + 1, best_pos + best_length


def main():
    transmission_files = ['transmission1.txt', 'transmission2.txt']
    mcode_files = ['mcode1.txt', 'mcode2.txt', 'mcode3.txt']

    transmissions = [read_file(file) for file in transmission_files]
    mcodes = [read_file(file) for file in mcode_files]

    # Buscar patrones mcode en transmisiones
    print("PARTE 1: Búsqueda de Patrones mcode en Transmisiones")
    for t_index, transmission in enumerate(transmissions):
        for m_index, mcode in enumerate(mcodes):
            contains = kmp(transmission, mcode)
            if contains:
                print(f"transmission{t_index + 1}.txt contains mcode{m_index + 1}.txt: True")
            else:
                print(f"transmission{t_index + 1}.txt does not contain mcode{m_index + 1}.txt: False")

    # Buscar palíndromos en transmisiones
    print("PARTE 2: Palíndromos Más Largos en Transmisiones")
    for t_index, transmission in enumerate(transmissions):
        palindrome = manacher(transmission)
        start_pos = transmission.index(palindrome) + 1
        end_pos = start_pos + len(palindrome) - 1
        print(f"Palíndromo más largo en transmission{t_index + 1}.txt abarca desde tiene posicionInicial={start_pos} hasta posicionFinal={end_pos}")

    # Encontrar el substring común más largo entre las dos transmisiones
    print("PARTE 3: Substring Común Más Largo entre Transmisiones")
    substring_comun = lcs(transmissions[0], transmissions[1])
    print(f"Substring con posicionInicial={substring_comun[0]} y posicionFinal={substring_comun[1]}")

if __name__ == "__main__":
    main()
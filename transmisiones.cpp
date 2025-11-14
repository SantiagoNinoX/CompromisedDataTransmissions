// E1: Transmisiones de Datos Comprometidas.
// Autores: Santiago Ramírez Niño (A01665906),
// Alejandro Ignacio Vargas Cruz (A01659714) y
// Omar Llano Tostado (A01660505).
// Materia: Análisis de Algoritmos Avanzados.
// Profesor: Dr. Salvador E. Venegas-Andraca.
// Fecha de entrega: 06 de noviembre de 2025.

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

// ========== FUNCIÓN PARA SUBSTRING COMÚN MÁS LARGO ==========
const long long BASE = 256;
const long long MOD = 1e9 + 7;

unordered_map<long long, vector<int>> get_hashes(const string& s, int length) {
    unordered_map<long long, vector<int>> hashes;
    
    if (length == 0 || length > (int)s.length()) {
        return hashes;
    }
    
    int n = s.length();
    long long h = 0;
    long long power = 1;
    
    // Hash inicial
    for (int i = 0; i < length; i++) {
        h = (h * BASE + (unsigned char)s[i]) % MOD;
        if (i < length - 1) {
            power = (power * BASE) % MOD;
        }
    }
    
    hashes[h].push_back(0);
    
    // Rolling hash
    for (int i = 1; i <= n - length; i++) {
        h = (h - (unsigned char)s[i - 1] * power % MOD + MOD) % MOD;
        h = (h * BASE + (unsigned char)s[i + length - 1]) % MOD;
        hashes[h].push_back(i);
    }
    
    return hashes;
}

pair<bool, int> check_length(const string& s1, const string& s2, int length) {
    if (length == 0) return {true, 0};
    
    auto hashes1 = get_hashes(s1, length);
    auto hashes2 = get_hashes(s2, length);
    
    for (const auto& p : hashes1) {
        long long h = p.first;
        
        auto it = hashes2.find(h);
        if (it != hashes2.end()) {
            // Verificar colisiones
            for (int pos1 : p.second) {
                for (int pos2 : it->second) {
                    bool match = true;
                    for (int k = 0; k < length; k++) {
                        if (s1[pos1 + k] != s2[pos2 + k]) {
                            match = false;
                            break;
                        }
                    }
                    if (match) {
                        return {true, pos1};
                    }
                }
            }
        }
    }
    
    return {false, -1};
}

pair<int, int> lcs_binary_search(const string& s1, const string& s2) {
    int n1 = s1.length();
    int n2 = s2.length();
    
    if (n1 == 0 || n2 == 0) {
        return {1, 0};
    }
    
    int left = 1, right = min(n1, n2);
    int best_length = 0;
    int best_pos = 0;
    
    while (left <= right) {
        int mid = left + (right - left) / 2;
        pair<bool, int> result = check_length(s1, s2, mid);
        
        if (result.first) {
            best_length = mid;
            best_pos = result.second;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    
    if (best_length == 0) {
        return {1, 0};
    }
    
    return {best_pos + 1, best_pos + best_length};
}

//FUNCIÓN PARA LEER ARCHIVOS
string read_file(const string& filename) {
    ifstream file(filename);
    string content, line;
    
    if (!file.is_open()) {
        cerr << "Error: No se pudo abrir " << filename << endl;
        return "";
    }
    
    while (getline(file, line)) {
        content += line;
    }
    
    file.close();
    return content;
}

int main() {
    // Leer archivos
    string trans1 = read_file("transmission1.txt");
    string trans2 = read_file("transmission2.txt");
    
    vector<string> transmissions = {trans1, trans2};
    
    // PARTE 3: Substring común más largo entre las dos transmisiones
    cout << "PARTE 3: Substring Común Más Largo entre Transmisiones" << endl;
    auto [start, end] = lcs_binary_search(trans1, trans2);
    cout << start << " " << end << endl;
    
    return 0;
}
# Cäsar-Chiffre in einer Linux Konsole

- Einen Text verschlüsseln:
  ```sh
  echo "HALLO LERNER." | ./caesar.py 7
  ```

- Einen Text entschlüsseln:
  ```sh
  echo "OHSSV SLYULY." | ./caesar.py -7
  ```

- Eine Textdatei verschlüsseln:
  ```sh
  cat plain.txt | ./caesar.py 7
  ```

- Eine Textdatei entschlüsseln:
  ```sh
  cat crypt.txt | ./caesar.py -7
  ```

- Eine Brute-Force Attacke durchführen.
  ```sh
  ./brute-force.sh crypt.txt
  ```
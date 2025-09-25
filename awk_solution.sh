
awk -F',' '{print $1","$2","$4}' data.csv > output.csv
echo "Файл output.csv создан."

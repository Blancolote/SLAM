import os
import pandas as pd
from PIL import Image

def repairPath(path):
        parts = path.split("/")
        change = parts[3]
        parts_change = change.split("-")
        parts[3] = parts_change[0]+'-NA-'+parts_change[1]
        return parts[3]

def createRepresentativeCVS(csv_Boxes, csv_groups, carpeta_pacientes):
        
    ids = []
    intermedia = []
    x_array = []
    y_array = []
    width = []
    heigth = []
    volume_array = []
    slice_representativo = []
    clasificacion = []
    width_img = []
    heigth_img = []
    
    groups = pd.read_csv(csv_groups)
    boxes = pd.read_csv(csv_Boxes)
    dic_anomalias = {}

    for patient, slice, x , y , w, h, volume in zip(boxes['PatientID'], boxes['Slice'], boxes['X'],boxes['Y'], boxes['Width'], boxes['Height'], boxes['VolumeSlices']):
        dic_anomalias[(patient,volume)] = [slice, x , y, w ,h]
   
    lista_pacientes = os.listdir(carpeta_pacientes)
    for paciente in lista_pacientes:

        carpetas_intermedias = os.path.join(carpeta_pacientes, paciente)
        lista_carpetas_intermedias = os.listdir(carpetas_intermedias)


        if paciente in boxes['PatientID'].values:

            for carpeta_intermedia in lista_carpetas_intermedias:
                
                carpeta_img = os.path.join(carpetas_intermedias, carpeta_intermedia)

                first_img = os.path.join(carpeta_img,os.listdir(carpeta_img)[0])

                ancho, largo = Image.open(first_img).size
                
                num_slices = len(os.listdir(carpeta_img))
                
                intermedia.append(carpeta_intermedia)
                volume_array.append(num_slices)
                ids.append(paciente)
                
                slice_representativo.append(dic_anomalias[(paciente, num_slices)][0])
                x_array.append(dic_anomalias[(paciente,num_slices)][1])
                y_array.append(dic_anomalias[(paciente,num_slices)][2])
                width.append(dic_anomalias[(paciente,num_slices)][3])
                heigth.append(dic_anomalias[(paciente,num_slices)][4])
                clasificacion.append(1)
                width_img.append(ancho)
                heigth_img.append(largo)
               
                
                
        else:
             
             for carpeta in lista_carpetas_intermedias:

                carpeta_img = os.path.join(carpetas_intermedias,carpeta)
                
                num_slices = len(os.listdir(carpeta_img))

                first_img = os.path.join(carpeta_img,os.listdir(carpeta_img)[0])

                ancho, largo = Image.open(first_img).size

                volume_array.append(num_slices)
                slice_representativo.append(num_slices)
                ids.append(paciente)
                intermedia.append(carpeta)
                diagnosis = groups.loc[groups["PatientID"] == paciente, "Actionable"].values[0]
                if diagnosis==1:
                    x_array.append(ancho)
                    y_array.append(0)
                    width.append(ancho)
                    heigth.append(largo)
                    clasificacion.append(1)
                else:
                    x_array.append(-1)
                    y_array.append(-1)
                    width.append(-1)
                    heigth.append(-1)
                    clasificacion.append(0)
                width_img.append(ancho)
                heigth_img.append(largo)


    

    output = pd.DataFrame({
          'PatientID': ids,
          'Intermedia': intermedia,
          'Slice_representativo': slice_representativo,
          'X': x_array,
          'Y': y_array ,
          'Width': width,
          'Height': heigth,
          'VolumeSlice': volume_array,
          'Clasificacion': clasificacion,
          'Original_width': width_img,
          'Original_height': heigth_img
    })
    
    output.to_csv(r'C:\Users\samue\Documents\UNI\TFG\csv_split\slices.csv')



if __name__=='__main__':
     csv_boxes = r''
     carpeta_pacientes = r''
     groups = r'' 

     createRepresentativeCVS(csv_boxes, groups ,carpeta_pacientes)

            





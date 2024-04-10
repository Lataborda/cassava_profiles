
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
from streamlit_folium import st_folium
from PIL import Image
from graphviz import Digraph
from streamlit_shadcn_ui import slider, input, textarea, radio_group, switch
import streamlit_shadcn_ui as ui

import folium


header = st.container()
MS = st.container() #Consumer Market segments
SMPS = st.container() #segments of cassava seed products
BCP = st.container() #Boild cassava preference
LQD = st.container() #Laboratory Quality data
PP =  st.container() #Product profile


with header:

	st.header('Preference and quality profiles by market segment for cassava in Colombia',divider='blue')
	st.markdown('With this tool you will be able to iterate between: 1) the segments of cassava seed products in Colombia :blue[(SMPS)], 2) the consumer market segments :blue[(MS)] of cassava consumption and 3) the main quality characteristics required in each segment :blue[(TTP)]')
	
	st.divider()
	st.write(' 👈To the left, you will find a menu with the different data visualization options used for the creation of quality and preference profiles')
	st.divider()
	
	DD = st.sidebar.radio(
	    "Select the type of data you want to display",
	    ["**Consumer market segments (MS)**", "**Segments of cassava seed products (SMPS)**", "**Boiled cassava preference**", "**Laboratory quality data**","**Product profile**"],
	    captions = ["Main consumers of cassava in Colombia, areas allocated to each segment", "Varieties most commonly used for each market segment and their locations", "Main preference traits for boild cassava", "laboratory quality data for sweet and industria cassava","Product profile"])

with MS:
		
	
	if DD == "**Consumer market segments (MS)**":
	    
		st.subheader('Consumer market segments (MS)')
		st.markdown("The following diagram represents the two main sets of cassava market segments. These are commonly referred to as 'sweet cassava' and 'Sour or industrial cassava'. The scheme specifies the amounts of cassava hectares planted in 2022 for each of the segments presented.")
		  
		  #Diagrama de flujo

		def create_flowchart():
		    dot = Digraph()
		    dot.node('A', 'SMPS')
		    dot.node('B', 'Sour/Industrial')
		    dot.node('C', 'Sweets',shape='diamond')
		    dot.node('D', 'Low-processing derivatives')
		    dot.node('E', 'Native Starch')
		    dot.node('F', 'Fermented Starch')
		    dot.node('G', 'Cassava chips')
		    dot.node('H', 'Boild cassava')
		    dot.node('I', 'Fried, chips, croquettes, frozen, paraffinized...', shape='box')
		    dot.node('J', 'Food industry', shape='box')
		    dot.node('K', 'Bakeries', shape='box')
		    dot.node('L', 'Animal feed', shape='box')


		    dot.edge('A', 'C', label="173.260 ha")
		    dot.edge('A', 'B', label="13.935 ha")
		    dot.edge('C', 'D', label="23.600 ha")
		    dot.edge('C', 'H', label="149.670 ha")
		    dot.edge('B', 'E', label="5.700 ha" )
		    dot.edge('B', 'F', label="3.639 ha")
		    dot.edge('B', 'G',label="4.596 ha")
		    dot.edge('D', 'I')
		    dot.edge('E', 'J')
		    dot.edge('F', 'K')
		    dot.edge('G', 'L')
	    
		    return dot

			# Crear el diagrama de flujo
		flowchart = create_flowchart()

			# Mostrar el diagrama de flujo en Streamlit
		st.graphviz_chart(flowchart)

		###Select DATA TO DISPLAY
		st.divider()

		#SWEET CASSAVA DATA
		
		
		ui.badges(badge_list=[("To know the cassava production (ha) by segment (main group) and by region (department) please select each of the following options:", "secundary")], class_name="flex gap-2", key="main_badges1")
		OP = ui.tabs(options=['Sweets', 'Sour/Industrial'], default_value='Sweets', key="Sweets")
			
		
		st.divider()

		if OP == "Sweets":

			## GRAFICA
			
			st.header("Areas (ha) of sweets_cassava(ha) by department")

			df = pd.read_csv("data/Pd11.csv", usecols=["Departament", "sweets_cassava(ha)"])
			Departament = df["Departament"]
			area = df["sweets_cassava(ha)"]

			# Ordena los datos por departamento
			df = df.sort_values(by="Departament")

			# Crea la figura
			fig, ax = plt.subplots()

			# Gráfica de barras
			ax.bar(Departament, area)

			# Personaliza la gráfica
			ax.set_xlabel("Departament")
			ax.set_ylabel("sweets_cassava(ha)")
			ax.set_title("Sweet cassava area by Department")

			
			# Ajustar el tamaño de la fuente
			plt.xticks(fontsize=6)

			# Rotar las etiquetas
			plt.xticks(rotation=90)

			# Ajustar el espaciado
			plt.subplots_adjust(bottom=0.2)

			
			# Mostrar la gráfica en Streamlit
			st.pyplot(fig)

			st.divider()
			#TABLA
			# Carga del archivo CSV
			df = pd.read_csv("data/Pd11.csv", usecols=["Departament", "sweets_cassava(ha)"])

			# Convertir el DataFrame a HTML, excluyendo el índice
			html = df.to_html(index=False)

			# Desplegar la tabla sin la columna de índice utilizando st.markdown
			st.markdown(html, unsafe_allow_html=True)

			st.page_link("https://sioc.minagricultura.gov.co/Yuca/Documentos/2021-03-31%20Cifras%20Sectoriales%20yuca.pdf", label="Source of information: Cadena Productiva de la Yuca Dirección de Cadenas Agrícolas y Forestales(2021)")
			st.page_link("https://sioc.minagricultura.gov.co/Yuca/Documentos/2020-12-31%20Cifras%20Sectoriales%20yuca.pdf", label="Subsector Productivo de la Yuca. Dirección de Cadenas Agrícolas y Forestales(2020)")
		
		elif OP == "Sour/Industrial":

			st.header("Areas (ha) of Sour_cassava(ha) by department")

			df = pd.read_csv("data/Pd11.csv", usecols=["Departament", "industria_cassava(ha)"])
			Departament = df["Departament"]
			area = df["industria_cassava(ha)"]

			# Ordena los datos por departamento
			df = df.sort_values(by="Departament")

			# Crea la figura
			fig, ax = plt.subplots()

			# Gráfica de barras
			ax.bar(Departament, area)

			# Personaliza la gráfica
			ax.set_xlabel("Departament")
			ax.set_ylabel("Industrial_cassava(ha)")
			ax.set_title("Industrial cassava area by Department")

			
			# Ajustar el tamaño de la fuente
			plt.xticks(fontsize=6)

			# Rotar las etiquetas
			plt.xticks(rotation=90)

			# Ajustar el espaciado
			plt.subplots_adjust(bottom=0.2)

			
			# Mostrar la gráfica en Streamlit
			st.pyplot(fig)

			st.divider()
			#TABLA
			
			# Carga del archivo CSV
			df = pd.read_csv("data/Pd11.csv", usecols=["Departament", "industria_cassava(ha)"])

			# Suprimir las filas donde hay valores faltantes
			df_clean = df.dropna(subset=["Departament", "industria_cassava(ha)"])

			# Redondear los valores numéricos a 0 decimales y convertir a entero
			df_clean["industria_cassava(ha)"] = df_clean["industria_cassava(ha)"].round(0).astype(int)

			# Convertir el DataFrame a HTML, excluyendo el índice
			html = df_clean.to_html(index=False)

			# Desplegar la tabla sin la columna de índice utilizando st.markdown
			st.markdown(html, unsafe_allow_html=True)

			st.page_link("https://sioc.minagricultura.gov.co/Yuca/Documentos/2021-03-31%20Cifras%20Sectoriales%20yuca.pdf", label="Source of information: Cadena Productiva de la Yuca Dirección de Cadenas Agrícolas y Forestales(2021)")
			st.page_link("https://sioc.minagricultura.gov.co/Yuca/Documentos/2020-12-31%20Cifras%20Sectoriales%20yuca.pdf", label="Subsector Productivo de la Yuca. Dirección de Cadenas Agrícolas y Forestales(2020)")
		

with SMPS:

	if DD == "**Segments of cassava seed products (SMPS)**":

			ui.badges(badge_list=[("To know the location of the main Segments of cassava seed products (SMPS) in Colombia, please select the following options:", "secundary")], class_name="flex gap-2", key="main_badges1")
			LO = ui.tabs(options=['Sweets', 'Sour/Industrial'], default_value='Sweets', key="Sweets")
			
			#LO = st.radio(
		    #"To know the location of the main Segments of cassava seed products (SMPS) in Colombia, please select the following options:",
		    #["Sweets","Sour/Industrial"],
		    #captions = ["Location of the main sweets_cassava seeds","Location of the main Sour/Industrial cassava seeds"])

			if LO == "Sweets":

				st.subheader("Location of the main sweet cassava commercial varieties")
				st.caption('click on each point to see the referent variety of its respective region')

				#VARIEDADES DE MESA UBICACIÓN
				m = folium.Map([5.336683, -75.589267], zoom_start=5.50)

				folium.Marker(
				    location=[9.842275016240356, -75.15471855351905],
				    popup=folium.Popup("Venezolana in Caribe", parse_html=True, max_width=100),
				).add_to(m)

				folium.Marker(
				    location=[2.755859, -76.624426],
				    popup=folium.Popup("Algodona in Cauca", parse_html=True, max_width="100%"),
				).add_to(m)

				folium.Marker(
				    location=[3.566271, -73.686723],
				    popup=folium.Popup("Brasilera in Llanos", parse_html=True, max_width="100%"),
				).add_to(m)

				folium.Marker(
				    location=[1.784186, -78.797162],
				    popup=folium.Popup("Yema de huevo(Yellow) in Pacifico Tumaco", parse_html=True, max_width="100%"),
				).add_to(m)

				folium.Marker(
				    location=[1.021240, -76.759270],
				    popup=folium.Popup("Yema de huevo(Yellow) in Putumayo", parse_html=True, max_width="100%"),
				).add_to(m)

				folium.Marker(
				    location=[4.555275, -75.681922],
				    popup=folium.Popup("Chirosa and Sietemesina in Caldas/Quindio", parse_html=True, max_width="100%"),
				).add_to(m)

				# Render the Folium map using st_folium
				folium_map = st_folium(m, width=400, height=550,)


			if LO == "Sour/Industrial":

				st.subheader("Location of the main Sour/Industrial cassava commercial varieties")
				st.caption('click on each point to see the referent variety of its respective region')

				#VARIEDADES DE MESA UBICACIÓN
				m = folium.Map([5.336683, -75.589267], zoom_start=5.50)

				folium.Marker(
				    location=[9.319316, -75.321742],
				    popup=folium.Popup("Mtat, Belloti, and Burrona in Caribe", parse_html=True, max_width=100),
				).add_to(m)

				folium.Marker(
				    location=[2.755859, -76.624426],
				    popup=folium.Popup("ICA48, Amarga and Algodona in Cauca", parse_html=True, max_width="100%"),
				).add_to(m)

				
				# Render the Folium map using st_folium
				folium_map = st_folium(m, width=400, height=550,)


with BCP:

	if DD == "**Boiled cassava preference**":
			
			st.subheader("Consumer preference traits for boiled cassava")	
			st.write('The following is a summary of the data obtained in 380 surveys, where the negative and positive traits at the time of purchasing and eating cassava were consulted. ')
			st.divider()
			
			#moment
			moment = st.selectbox('***Select the moment:***',options = ['purchasing cassava', "Eating Cassava"])
			
			if moment == "Eating Cassava":

				st.write('***Result of open answers: How is the cassava that consumer likes most and less...***')

				#Traits cassava (open responses) at eating moment
				col1, col2 = st.columns(2)

				with col1:
				   
							   
					Trait = ["Hard","Fibrous","Bitter","Glassy","Undesirable color","Dry","Sticky","Non-floury","cohesiva"]
					data_df = pd.DataFrame(
					    {
					        "Undesirable traits": Trait,
					        "freq": [50,18,13,8,6,4,1,0,0],
					    }
					)

					# Establecer la columna "index_letras" como índice
					
					data_df = data_df.set_index("Undesirable traits")

					# Mostrar el editor de datos con el nuevo índice
					st.data_editor(
					    data_df,
					    column_config={
					        "freq": st.column_config.ProgressColumn(
					            "Frequency",
					            help="Response frequency",
					            format="%f%%", 
					            min_value=0,
					            max_value=100,
					        ),
					    },
					)

				with col2:
				  
				   
					Trait1 = ["Smooth","Floury","desired color","Friable","not bitter","Non-fibrous","Wet","non-sticky","non-glassy"]
					data_df1 = pd.DataFrame(
					    {
					        "Desirable traits": Trait1,
					        "sales": [49,22,8,7,5,5,3,0,0],
					    }
					)

					# Establecer la columna "index_letras" como índice
					data_df1 = data_df1.set_index("Desirable traits")

					# Mostrar el editor de datos con el nuevo índice
					st.data_editor(
					    data_df1,
					    column_config={
					        "sales": st.column_config.ProgressColumn(
					            "Frequency",
					            help="Response frequency",
					            format="%f%%", 
					            min_value=0,
					            max_value=100,
					        ),
					    },
					)
				
				st.divider()
				st.write('***Result of closed answers: How is the preference for each trait***')
				st.image('data/pe1.png', caption="Color preference")
				st.divider()
				st.image('data/pe2.png', caption="Friability preference")
				st.divider()
				st.image('data/pe3.png', caption="Bitter, Fibrous and Sitcky preference")
				st.divider()
				st.image('data/pe4.png', caption="Hardness, Floury and Dry preference")

			elif moment == ("purchasing cassava"): 
				
				st.write('***Result of open answers: How is the cassava that consumer likes most and less...***')
				#Traits cassava (open responses) at purchasing moment
				col1, col2 = st.columns(2)

				with col1:
				   
							   
					Trait2 = ["With Deterioration","Hard","Undesirable size","Undesirable pulp color","Undesirable form","Undesirable skin color"]
					data_df = pd.DataFrame(
					    {
					        "Undesirable traits": Trait2,
					        "freq": [48,18,17,7,6,4],
					    }
					)

					# Establecer la columna "index_letras" como índice
					
					data_df = data_df.set_index("Undesirable traits")

					# Mostrar el editor de datos con el nuevo índice
					st.data_editor(
					    data_df,
					    column_config={
					        "freq": st.column_config.ProgressColumn(
					            "Frequency",
					            help="Response frequency",
					            format="%f%%", 
					            min_value=0,
					            max_value=100,
					        ),
					    },
					)

				with col2:
				  
				   
					Trait1 = ["No deterioration","Desirable pulp color","Smooth","Desirable size","Desirable form","Desirable skin color"]
					data_df1 = pd.DataFrame(
					    {
					        "Desirable traits": Trait1,
					        "sales": [36,26,12,10,10,6],
					    }
					)

					# Establecer la columna "index_letras" como índice
					data_df1 = data_df1.set_index("Desirable traits")

					# Mostrar el editor de datos con el nuevo índice
					st.data_editor(
					    data_df1,
					    column_config={
					        "sales": st.column_config.ProgressColumn(
					            "Frequency",
					            help="Response frequency",
					            format="%f%%", 
					            min_value=0,
					            max_value=100,
					        ),
					    },
					)
				st.divider()
				st.write('***Result of closed answers: How is the preference for each trait***')
				st.image('data/pu1.png', caption="Preferred root length")
				st.divider()
				st.image('data/pu2.png', caption="Preferred peduncle length")
				st.divider()
				st.image('data/pu3.png', caption="Preferred skin color")
				st.divider()
				st.image('data/pu4.png', caption="Preferred pulp color")
				st.divider()
				st.image('data/pu5.png', caption="Preferred root form")


with LQD:

	if DD == "**Laboratory quality data**":


		st.header("Laboratory data on quality variables of commercial cassava referents")
		ui.badges(badge_list=[("To view the quality test data for commercial varieties in each market segment select one of the following options ", "secundary")], class_name="flex gap-2", key="main_badges1")
		LAP = ui.tabs(options=['Sweets', 'Sour/Industrial'], default_value='Sweets', key="Sweets")
			
		if LAP == "Sweets":
			

			def cargar_datos(ruta_archivo):
				df = pd.read_csv("data/variety7.csv", sep=None, engine='python', header=0, index_col=0)
				return df


			def main():
			    #st.title('Visualizador de CSV con Streamlit')

			    # Definir la ruta del archivo dentro de la carpeta 'data'
			    ruta_archivo = 'data/variety7.csv'
		    
			    try:
			        df = cargar_datos(ruta_archivo)
			        st.write("Laboratory test results:")
			        st.dataframe(df)
			    
			    except Exception as e:
			        st.error(f"Se produjo un error al cargar el archivo: {e}")

			if __name__ == "__main__":
			    main()

			st.divider()

			# grafico de barras iterando variables

			# Cargar datos
			data_path = 'data/variety7.csv'  # Actualiza con la ruta a tu archivo CSV
			data = pd.read_csv(data_path)

			# Título de la aplicación
			st.header("Variety Data Visualization")

			# Asumiendo que las columnas de interés son las 5 a 9, ajusta según tus datos exactos
			# Cambia ['Columna5', 'Columna6', ..., 'Columna9'] por los nombres reales de tus columnas si es necesario
			options = data.columns[4:9]  # Ajusta los índices según tus necesidades

			# Selector de variables para el eje Y utilizando st.selectbox
			option = st.selectbox(
			    'Select the variable you want to compare among the varieties',
			    options  # Usa el rango de columnas ajustado
			)

			# Verificación para asegurar que se seleccionó una opción
			if not option:
			    st.error("Por favor, selecciona una variable para el eje Y.")
			else:
			    # Crear la gráfica de barras
			    fig, ax = plt.subplots()
			    ax.bar(data['Variety'], data[option], label=option)
			    ax.set_xlabel('Variety')
			    ax.set_ylabel(option)
			    ax.set_title(f'Variedad vs. {option}')
			    ax.legend()
			    # Rotar los títulos del eje X
			    ax.set_xticklabels(data['Variety'], rotation=90)
			    st.pyplot(fig)



		elif LAP == "Sour/Industrial":

			
			def cargar_datos(ruta_archivo):
				df = pd.read_csv("data/sour1.csv", sep=None, engine='python', header=0, index_col=0)
				return df


			def main():
			    #st.title('Visualizador de CSV con Streamlit')

			    # Definir la ruta del archivo dentro de la carpeta 'data'
			    ruta_archivo = 'data/sour1.csv'
		    
			    try:
			        df = cargar_datos(ruta_archivo)
			        st.write("Laboratory test results:")
			        st.dataframe(df)
			    
			    except Exception as e:
			        st.error(f"Se produjo un error al cargar el archivo: {e}")

			if __name__ == "__main__":
			    main()

			st.divider()

			# CGRAFICAS BARRAS POR VARIABLES AMARGAS
			data_path = 'data/sour1.csv'  # Actualiza con la ruta a tu archivo CSV
			data = pd.read_csv(data_path)

			# Título de la aplicación
			st.header("Variety Data Visualization")

			# Asumiendo que las columnas de interés son las 5 a 9, ajusta según tus datos exactos
			# Cambia ['Columna5', 'Columna6', ..., 'Columna9'] por los nombres reales de tus columnas si es necesario
			options = data.columns[4:9]  # Ajusta los índices según tus necesidades

			# Selector de variables para el eje Y utilizando st.selectbox
			option = st.selectbox(
			    'Select the variable you want to compare among the varieties',
			    options  # Usa el rango de columnas ajustado
			)

			# Verificación para asegurar que se seleccionó una opción
			if not option:
			    st.error("Por favor, selecciona una variable para el eje Y.")
			else:
			    # Crear la gráfica de barras
			    fig, ax = plt.subplots()
			    ax.bar(data['Variety'], data[option], label=option)
			    ax.set_xlabel('Variety')
			    ax.set_ylabel(option)
			    ax.set_title(f'Variedad vs. {option}')
			    ax.legend()
			    # Rotar los títulos del eje X
			    ax.set_xticklabels(data['Variety'], rotation=90)
			    st.pyplot(fig)

with PP:

	if DD == "**Product profile**":

		st.header("Cassava Product profile")
		#ui.badges(badge_list=[("Product profile", "destructive")], class_name="flex gap-2", key="main_badges1")
		st.caption("This is a proposed technical sheet for the different uses of cassava in Colombia. The values shown on the cards correspond to the averages of measurements made on commercial varieties. ")
		
		st.subheader("Technical sheet")

		TS = ui.tabs(options=['Boiled cassava', 'Sour cassava'], default_value='Boiled cassava', key="Boiled cassava")

		if TS == "Boiled cassava":

	       	##promedios
			df = pd.read_csv('data/variety7.csv')

			df.columns = df.columns.str.strip()

			# Calcula el promedios 
			p5 = df.iloc[:, 4].mean()#Dry matter
			p6 = df.iloc[:, 5].mean()#b_carotene content (ug/g)
			p7 = df.iloc[:, 6].mean()#Total_carotenes_(ug/g)
			p8= df.iloc[:, 7].mean()
			p9 = round(df.iloc[:, 8].mean(), 1)


			
			cols = st.columns(3)
			with cols[0]:
			     #with ui.card():
			       #  ui.element()
			    ui.card(title="Dry matter", content=p5, description="Content percentage", key="card1").render()
			with cols[1]:
			    ui.card(title="b_carotene content", content=p6, description="(ug/g) NIRS 400-2500 nm", key="card2").render()
			with cols[2]:
			    ui.card(title="Total_carotenes", content=p7, description="(ug/g) NIRS 400-2500 nm", key="card3").render()
			
			st.divider()

			cols1 = st.columns(3)
			with cols1[0]:
			    ui.card(title="Boiling estimation", content=p8, description="minute_boiled root", key="card4").render()
			with cols1[1]:
			    ui.card(title="Cyanide", content=p9, description="(ug/g)ug/g wet basis", key="card5").render()
			with cols1[2]:
			    ui.card(title="Color", content="White", description="Acceptance probability > 80%", key="card6").render()


		if TS == "Sour cassava":

			
			#with ui.element("div", className="flex gap-2", key="buttons_group1"):
			  # ui.element("button", text="Get Started", className="btn btn-primary", key="btn1")
			  # ui.element("link_button", text="Github", url="https://github.com/ObservedObserver/streamlit-shadcn-ui", variant="outline", key="btn2")
				
			##promedios
			df = pd.read_csv('data/sour1.csv')

			df.columns = df.columns.str.strip()

			# Calcula el promedios 
			pr4 = round(df.iloc[:, 3].mean(),1)#Dry matter
			pr5 = df.iloc[:, 4].mean()#Starch contet (%)
			pr6 = round(df.iloc[:, 5].mean(),1)#amilosa
			pr7= round(df.iloc[:, 6].mean(),1) #pasting time
			pr8 = round(df.iloc[:, 7].mean(),1) #pasting temperature
			pr9 = round(df.iloc[:, 8].mean(),1) #peak viscosity

			
			cols = st.columns(3)
			with cols[0]:
			     #with ui.card():
			       #  ui.element()
			    ui.card(title="Dry matter", content=f"{pr4}%", description="(%) of the roost", key="card1").render()
			with cols[1]:
			    ui.card(title="Starch contet", content=f"{pr5}%", description="(%)of the roost", key="card2").render()
			with cols[2]:
			    ui.card(title="Amylose", content=f"{pr6}%", description="(%) of the starch", key="card3").render()
			
			st.divider()

			cols1 = st.columns(3)
			with cols1[0]:
			    ui.card(title="Starch pasting time", content=pr7, description="Time in minutes", key="card4").render()
			with cols1[1]:
			    ui.card(title="Starch pasting temperature", content=f"{pr6}⁰", description="Temperature in ⁰Celsius", key="card5").render()
			with cols1[2]:
			    ui.card(title="Starch peak viscosity", content=pr9, description="Centipoises (cp)", key="card6").render()





st.markdown('*Copyright (C) 2024 CIRAD, AGROSAVIA & CIAT*')
st.caption('**Authors: Alejandro Taborda, (latabordaa@unal.edu.co), Thierry Tran, Amparo Rosero, Katia Contreras, Luis Londoño, Alejandra Ospina, Jhon Moreno, Jorge Luna, Cristhian Duarte, Robert Andrade, Jhonatha Newby**')

	
	







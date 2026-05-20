#!/usr/bin/env python3
"""
Build interactive HTML guide for Gestión de Muestras Biológicas.
Style identical to biologia-molecular-guia, content from 41 PDFs.
"""
def sec(num, title, subs):
    return {"id": f"s{num.replace('.','')}", "num": num, "title": title, "content": subs}

units = [
  {
    "code": "U1",
    "title": "Análisis de la estructura organizativa del sector sanitario",
    "emoji": "🏥",
    "desc": "Sistemas sanitarios, organización administrativa, niveles asistenciales, laboratorios clínicos y fases del análisis",
    "sections": [
      sec("1.1", "Importancia y tipos de sistemas sanitarios", [
        ("Sistema sanitario", "", [
          "Conjunto de instituciones, personal especializado, normas y medios que proporcionan asistencia sanitaria a una población",
          "Objetivos: mejorar la salud, asegurar equidad en el acceso, estar legitimado ante la población"
        ]),
        ("Organización de un sistema sanitario", "grid", [
          "Financiación → Soporte económico (impuestos, cotizaciones, cuotas privadas)",
          "Provisión → Edificios, materiales, equipos, personal (pública, privada o mixta)",
          "Cobertura poblacional → Quién puede acceder al sistema",
          "Organización interna → Para que el sistema sea sostenible"
        ]),
        ("Tipos de sistemas sanitarios", "table", [
          ["Modelo", "Características", "Ejemplo"],
          ["Liberal", "Privado, financiación por seguros", "EE.UU. (parcial)"],
          ["Seguros Sociales", "Cotizaciones trabajadores/empresarios", "Alemania, Francia"],
          ["Nacional de Salud", "Impuestos generales, universal", "España (SNS), Reino Unido"],
          ["Mixto", "Combina elementos públicos y privados", "Varios países"]
        ])
      ]),
      sec("1.2", "Sistema sanitario español: SNS", [
        ("Ley General de Sanidad", "", [
          "Regula el Sistema Nacional de Salud (SNS) en España",
          "Principios: Universalidad, Atención integrada, Recursos, Participación, Financiación, Eficacia"
        ]),
        ("Organización administrativa", "flow", [
          "Nivel central → Ministerio de Sanidad: fija líneas generales de actuación del SNS",
          "Nivel autonómico → Consejería de Sanidad de cada CC.AA.: gestiona recursos",
          "Nivel área de salud → Unidad geográfica y funcional, bajo revisión de las CC.AA."
        ]),
        ("Prestaciones del SNS", "", [
          "Asistencia de medicina general y todas las especialidades (ordinaria y urgencia)",
          "Prestación farmacéutica extrahospitalaria",
          "Rehabilitación y transporte de enfermos",
          "Prótesis y vehículos para discapacitados",
          "Tratamiento y estancia en centros sanitarios"
        ]),
        ("Niveles asistenciales", "table", [
          ["Nivel", "Descripción", "Dónde se presta"],
          ["Atención Primaria", "Primer nivel, cercano y generalista. Prevención, promoción y problemas comunes", "Centros de salud"],
          ["Atención Especializada", "Segundo nivel, médicos especialistas, pruebas complejas y tratamientos avanzados", "Hospitales"],
          ["Atención Sociosanitaria", "Para pacientes con patologías crónicas que requieren cuidados prolongados", "Centros sociosanitarios"]
        ])
      ]),
      sec("1.3", "Organización del laboratorio de análisis clínico", [
        ("Core Lab (Laboratorio Central)", "", [
          "Laboratorio central automatizado que concentra muestras de distintos servicios",
          "Reduce costes y optimiza recursos",
          "Evita duplicidades y mejora calidad de resultados",
          "Mejora tiempos de respuesta"
        ]),
        ("Organigrama del laboratorio clínico", "flow", [
          "Dirección del laboratorio",
          "Facultativos especialistas: supervisan y validan resultados",
          "Técnicos de laboratorio: toman y analizan muestras, gestionan existencias",
          "Personal administrativo: registros, informes, contacto"
        ]),
        ("Funciones del técnico de laboratorio clínico", "", [
          "Gestionar existencias de material de laboratorio",
          "Mantener el laboratorio organizado y limpio (incluyendo eliminación de residuos)",
          "Preparar equipos y revisar su funcionamiento óptimo",
          "Toma y análisis de muestras",
          "Registro y examinación de resultados de experimentos",
          "Comunicación de resultados a facultativos",
          "Preparación de materiales de apoyo a la docencia",
          "Supervisión del personal en prácticas"
        ]),
        ("Funciones del técnico de anatomía patológica", "", [
          "Colaborar en la realización de necropsias clínicas o médico-legales",
          "Procesar muestras de material biológico para estudio por el patólogo",
          "Seleccionar y aportar datos para diagnóstico de citologías ginecológicas",
          "Realizar citologías de líquidos, secreciones, improntas y muestras no ginecológicas",
          "Registrar fotográficamente piezas y preparaciones",
          "Aplicar técnicas de inmunohistoquímica, inmunofluorescencia y biología molecular"
        ])
      ]),
      sec("1.4", "Fases de la determinación analítica", [
        ("Las tres fases", "flow", [
          "FASE PREANALÍTICA → Incluye desde la solicitud médica hasta que la muestra está lista en el laboratorio. Responsabilidad principal: médicos y enfermeros",
          "FASE ANALÍTICA → Abarca todos los procesos donde se manipula la muestra y se realizan análisis. Responsabilidad: técnicos de laboratorio",
          "FASE POSTANALÍTICA → Interpretación de resultados, elaboración de informes y conservación de muestras para repetir pruebas si es necesario"
        ]),
        ("Recorrido de una muestra (desde extracción hasta resultado)", "flow", [
          "1️⃣ Toma de muestras por personal especializado",
          "2️⃣ Pruebas POCT (punto de cuidados): resultados casi inmediatos en el centro de toma",
          "3️⃣ Laboratorios satélite: pruebas urgentes o rutinarias (<60 min)",
          "4️⃣ Laboratorio central: análisis complejos o especializados (pueden tardar días)",
          "5️⃣ Envío de resultados al centro de origen para interpretación"
        ])
      ]),
      sec("1.5", "Aspectos económicos en laboratorios", [
        ("Centros concertados", "", [
          "Centros privados que han llegado a acuerdos con entidades públicas",
          "Prestan servicio con financiación parcial o total del Estado"
        ]),
        ("Gestión de almacén de suministros", "table", [
          ["Sistema", "Significado", "Uso en sanidad"],
          ["FIFO", "First In, First Out (lo que entró primero se usa primero)", "Muy común: evita caducidades"],
          ["LIFO", "Last In, First Out (lo que entró último se usa primero)", "Menos común en sanidad"],
          ["PMP", "Precio Medio Ponderado", "Estimación de costes según cantidades"]
        ]),
        ("Materiales en el laboratorio", "", [
          "Fungibles (desechables): uso limitado, se renuevan periódicamente (guantes, puntas, tubos)",
          "No fungibles (reutilizables): larga vida útil (microscopios, centrifugadoras, neveras)"
        ])
      ]),
    ]
  },
  {
    "code": "U2",
    "title": "Identificación de la documentación del laboratorio",
    "emoji": "📋",
    "desc": "Recepción, registro, trazabilidad, sistemas informáticos, documentación gráfica, bioética y gestión de almacén",
    "sections": [
      sec("2.1", "Recepción, registro y clasificación de muestras", [
        ("Flujo de trabajo en el laboratorio", "flow", [
          "1️⃣ Recepción de muestras",
          "2️⃣ Registro de muestras",
          "3️⃣ Clasificación de muestras",
          "4️⃣ Procesamiento de muestras",
          "5️⃣ Realización de análisis",
          "6️⃣ Validación facultativa",
          "7️⃣ Elaboración de informe",
          "8️⃣ Distribución y entrega",
          "9️⃣ Custodia y conservación de muestras"
        ]),
        ("Recepción", "", [
          "Verificar que la muestra llega en condiciones adecuadas",
          "Comprobar que la solicitud coincide con la muestra",
          "Dato imprescindible: nombre del paciente"
        ]),
        ("Registro", "", [
          "Introducir la muestra en el sistema con todos los datos del paciente",
          "Asignar un identificador único"
        ]),
        ("Clasificación", "", [
          "Agrupar muestras según su naturaleza y las pruebas a realizar",
          "Distribuir a diferentes secciones o departamentos",
          "Alicuotado: reparto de la muestra en diferentes recipientes para distintos destinos"
        ]),
        ("Trazabilidad", "", [
          "Sistema que permite identificar y ubicar las muestras en cualquier etapa",
          "Registra determinaciones analíticas y responsables",
          "Fundamental para la calidad y seguridad del laboratorio"
        ])
      ]),
      sec("2.2", "Sistemas informáticos de gestión", [
        ("Bases de datos", "", [
          "Herramientas de software que permiten introducir información y relacionarla entre sí",
          "En el laboratorio clínico: registrar datos del paciente y agregar resultados de pruebas"
        ]),
        ("SIL - Sistemas de Información del Laboratorio", "", [
          "Sistemas compuestos por software + hardware para gestionar información",
          "Generan documentos de forma automatizada",
          "Funciones: 1️⃣ Registrar, 2️⃣ Procesar, 3️⃣ Almacenar, 4️⃣ Consultar"
        ])
      ]),
      sec("2.3", "Registro y archivo de documentación gráfica", [
        ("Imágenes macroscópicas", "", [
          "Muestran elementos observables a simple vista sin instrumentos",
          "Aportan información sobre aspecto y estado de tejidos y órganos"
        ]),
        ("Imágenes microscópicas (micrografías)", "", [
          "Más frecuentes que las macroscópicas en laboratorio",
          "Requieren microscopio para su obtención"
        ])
      ]),
      sec("2.4", "Documentos de normativa bioética", [
        ("LOPD - Ley Orgánica de Protección de Datos", "", [
          "Protege la confidencialidad de los datos de salud",
          "Datos especialmente protegidos: datos relativos a la salud",
          "Información genérica: procedimientos del laboratorio sin implicar pacientes",
          "Información personal: teléfonos, direcciones, resultados de pruebas"
        ]),
        ("Consentimiento informado", "", [
          "Documento que el paciente firma autorizando un procedimiento",
          "Características: voluntariedad, información clara, posibilidad de revocación",
          "NO es obligatorio en cualquier analítica (depende del nivel de invasividad)"
        ])
      ]),
      sec("2.5", "Documentación de almacén", [
        ("Ficha de almacén e inventario", "", [
          "Ficha de almacén: registro detallado de cada producto (proveedor, lote, caducidad, stock)",
          "Inventario: listado completo de existencias del laboratorio"
        ]),
        ("Albarán y factura", "", [
          "Albarán: documento que se firma como prueba de que una mercancía ha sido entregada",
          "Factura: documento comercial que detalla la compra y el importe"
        ])
      ])
    ]
  },
  {
    "code": "U3",
    "title": "Identificación de muestras biológicas",
    "emoji": "🧪",
    "desc": "Tipos de muestras, características, métodos de análisis, variabilidad preanalítica y errores en la manipulación",
    "sections": [
      sec("3.1", "Muestras biológicas y su clasificación", [
        ("Definición", "", [
          "Porciones tomadas de organismos vivos que reúnen las características fisicoquímicas de las partes a analizar"
        ]),
        ("Tipos de muestras", "table", [
          ["Tipo", "Estado", "Ejemplos"],
          ["Muestras líquidas", "Líquido", "Sangre, orina, LCR, líquido pleural"],
          ["Muestras de tejidos", "Sólido o semisólido", "Biopsias, piezas quirúrgicas"],
          ["Muestras citológicas", "Células libres", "Citología cérvico-vaginal, PAAF"]
        ]),
        ("Clasificación detallada de muestras líquidas", "table", [
          ["Categoría", "Definición", "Ejemplos", "Características"],
          ["Muestras líquidas corporales", "Líquidos producidos normalmente por el cuerpo", "Sangre, plasma, orina, líquido pleural", "Información general del organismo"],
          ["Secreciones", "Sustancias expulsadas para cumplir una función", "Esputo, saliva, secreción bronquial, gástrica", "Reflejan funcionamiento de órganos"],
          ["Exudados", "Líquidos anormales por alteración o patología", "Exudado pleural, peritoneal, purulento", "Composición variable, indican inflamación"]
        ])
      ]),
      sec("3.2", "Muestras de tejidos y citológicas", [
        ("Muestras de tejidos", "", [
          "Porciones de órganos u otras partes del cuerpo",
          "La mayoría son sólidas o semisólidas",
          "Se obtienen por biopsias (métodos invasivos)",
          "Informan sobre el estado de composición y estructura"
        ]),
        ("Muestras citológicas", "", [
          "Soluciones con células libres extraídas de zonas donde se desprenden fácilmente"
        ]),
        ("Citología descamativa vs aspirativa", "table", [
          ["Aspecto", "Citología Descamativa", "Citología Aspirativa"],
          ["Definición", "Células desprendidas espontáneamente o por raspado suave", "Células obtenidas mediante aguja con presión negativa"],
          ["Método", "Raspado/frotis con espátula, cepillo o hisopo", "Inserción de aguja fina con jeringa"],
          ["Invasividad", "No invasiva o mínimamente invasiva", "Levemente invasiva (requiere punción)"],
          ["Aplicaciones", "Cuello uterino (Papanicolaou), mucosa oral, tracto digestivo", "Tiroides, mama, ganglios linfáticos, órganos sólidos"],
          ["Finalidad", "Diagnóstico de lesiones superficiales o infecciones", "Diagnóstico de tumores, quistes o masas internas"]
        ])
      ]),
      sec("3.3", "Sustancias analizables y tipos de análisis", [
        ("Análisis cualitativo vs cuantitativo", "table", [
          ["Aspecto", "Análisis Cualitativo", "Análisis Cuantitativo"],
          ["Objetivo", "Identificar presencia o identidad de sustancias", "Medir cantidad o concentración"],
          ["Información", "Presencia/ausencia (qué hay)", "Cantidad (cuánto hay)"],
          ["Ejemplos", "Tinciones, estudios anatomopatológicos", "Análisis rutinarios de sangre, conteo celular"],
          ["Resultado", "Positivo/negativo, tipo de agente", "Valor numérico (concentración)"],
          ["Complejidad", "Generalmente más simple y rápida", "Requiere equipos especializados"]
        ])
      ]),
      sec("3.4", "Variabilidad preanalítica del paciente", [
        ("Factores fisiológicos", "grid", [
          ("Edad", "Los valores de referencia cambian con la edad del paciente"),
          ("Sexo", "Diferencias hormonales y hematológicas entre hombres y mujeres"),
          ("Embarazo", "Alteraciones en múltiples parámetros analíticos"),
          ("Ciclos biológicos", "Variaciones diarias, mensuales o estacionales"),
          ("Dieta", "Ayuno necesario para valores constantes de glucosa, lípidos, etc."),
          ("Estilo de vida", "Ejercicio intenso aumenta ácidos grasos y ácido láctico")
        ]),
        ("Factores en la toma de muestras", "table", [
          ["Factor", "Descripción", "Impacto"],
          ["Dieta", "Alimentación altera glucosa, albúmina, lípidos, ácido úrico", "Se recomienda ayuno previo"],
          ["Tiempo torniquete", "Uso prolongado durante extracción", "Concentra componentes y altera la muestra"],
          ["Sueros terapéuticos", "Paciente con vía intravenosa", "Tomar muestra en brazo contrario"],
          ["Ejercicio intenso", "Actividad física antes de la toma", "Aumenta ácidos grasos, alanina, ácido láctico"]
        ]),
        ("Interferencias analíticas", "table", [
          ["Interferencia", "Descripción", "Efecto"],
          ["Hemólisis", "Rotura de glóbulos rojos (hemoglobina >0,3 g/L)", "Altera valores, generalmente los aumenta"],
          ["Lipemia", "Altos niveles de lípidos por falta de ayuno", "Afecta determinación de varios analitos"],
          ["Fármacos", "Medicamentos que alteran resultados", "Cambian valores; informar y evaluar"],
          ["Drogas autorizadas", "Alcohol, tabaco, etc.", "Provocan alteraciones conocidas"]
        ]),
        ("Variabilidad según el sexo. Salud y enfermedad", "table", [
          ["Parámetro", "Diferencia"],
          ["Glóbulos rojos, hemoglobina, hematocrito", "Valores más altos en hombres que en mujeres"],
          ["Ferritina", "Clave en mujeres por pérdidas menstruales y embarazo"],
          ["PSA (Antígeno prostático específico)", "Presente solo en hombres, marcador cáncer de próstata"],
          ["Hormonas sexuales", "Mujeres: FSH, LH, estradiol, progesterona. Hombres: testosterona, SHBG"]
        ])
      ]),
      sec("3.5", "Errores en la manipulación preanalítica", [
        ("Principales errores", "table", [
          ["Error", "Descripción"],
          ["Análisis no pertinentes", "Pruebas innecesarias o en magnitudes incorrectas"],
          ["Ignorar características del paciente", "No considerar edad, sexo, medicación"],
          ["Incumplimiento del ayuno", "Paciente no ayuna antes de la toma"],
          ["Toma incorrecta de muestra", "Muestra obtenida de forma inadecuada"],
          ["Etiquetado incorrecto", "Muestra mal identificada"],
          ["Contaminación por mala manipulación", "Durante recolección o manipulación"],
          ["Contaminación en transporte", "Durante el traslado al laboratorio"],
          ["Mala conservación en transporte", "Condiciones inadecuadas de temperatura"]
        ])
      ])
    ]
  },
  {
    "code": "U4",
    "title": "Muestras de sangre",
    "emoji": "🩸",
    "desc": "Obtención de muestras, aditivos, anticoagulantes, interferencias, componentes sanguíneos y productos derivados",
    "sections": [
      sec("4.1", "Obtención de muestras sanguíneas", [
        ("Consideraciones previas", "grid", [
          ("Postura del paciente", "La posición afecta la concentración de la muestra. En pacientes encamados los componentes pueden aparecer 5-15% más concentrados"),
          ("Perfusiones y transfusiones", "Todos los componentes se alteran al introducir o extraer sangre. Tomar muestra en brazo contrario a la vía"),
          ("Intervenciones diagnósticas/terapéuticas", "Medicamentos pueden alterar los parámetros"),
          ("Momento de la toma", "Varía según el momento del día o del mes (mujeres)"),
          ("Dieta", "Impacto directo sobre glucosa, lípidos, etc. Ayuno necesario"),
          ("Método empleado", "Instrumentos y aditivos pueden alterar la muestra")
        ]),
        ("Materiales para extracción", "", [
          "Sistema de vacío (tubos con presión negativa)",
          "Agujas y adaptadores",
          "Torniquete, alcohol, algodón, gasas estériles",
          "Guantes, apósitos, contenedor de residuos"
        ]),
        ("Procedimiento de extracción venosa", "flow", [
          "1️⃣ Identificar al paciente",
          "2️⃣ Colocar torniquete y seleccionar vena",
          "3️⃣ Desinfectar la zona",
          "4️⃣ Insertar la aguja y extraer la muestra",
          "5️⃣ Retirar torniquete ANTES de retirar la aguja",
          "6️⃣ Retirar la aguja y presionar la zona",
          "7️⃣ Etiquetar los tubos correctamente"
        ]),
        ("Errores comunes y complicaciones", "table", [
          ["Situación", "Causa"],
          ["La sangre deja de fluir", "Venas colapsadas o mala colocación del tubo (sin presión negativa)"],
          ["Sangre insuficiente", "Torniquete demasiado apretado o posición inadecuada del brazo"],
          ["Hematoma", "Mala punción o no presionar después de retirar"],
          ["Hemólisis", "Agitar demasiado o aguja muy fina"]
        ])
      ]),
      sec("4.2", "Extracción arterial y capilar. Hemocultivos", [
        ("Extracción arterial", "", [
          "Utiliza jeringuillas especiales (gasometría, autollenado o aspiración)",
          "Uso: valoración del intercambio gaseoso en sangre",
          "Se usa tubo con heparina (anticoagulante)",
          "Análisis en menos de 30 minutos",
          "No agitar en exceso"
        ]),
        ("Extracción capilar", "", [
          "Punción cutánea para obtener sangre por capilaridad",
          "Volumen pequeño, ideal para niños pequeños",
          "Se descartan primeras gotas para evitar contaminación",
          "Método menos agresivo pero volumen limitado"
        ]),
        ("Hemocultivos", "table", [
          ["Característica", "Aeróbicos", "Anaeróbicos"],
          ["Condiciones", "Presencia de oxígeno", "Ausencia de oxígeno"],
          ["Patógenos", "Bacterias y hongos que necesitan oxígeno", "Bacterias que crecen sin oxígeno"],
          ["Tubo", "Diseñado para ambiente oxigenado", "Sellado para evitar oxígeno"],
          ["Uso clínico", "Infecciones por microorganismos aeróbicos", "Infecciones por anaerobios"]
        ])
      ]),
      sec("4.3", "Aditivos y código de color de tubos", [
        ("Tipos de aditivos", "table", [
          ["Aditivo", "Función", "Ejemplos", "Uso"],
          ["Anticoagulantes", "Evitan o retrasan la coagulación", "EDTA, Heparina, Citrato", "Hematología, bioquímica, coagulación"],
          ["Agentes estabilizantes", "Mantienen integridad del ARN", "Conservantes de ARN", "Análisis genéticos"],
          ["Gel separador", "Facilita separación del coágulo", "Geles de silicona", "Obtener suero limpio"]
        ]),
        ("Conservación aproximada según aditivo", "table", [
          ["Aditivo", "Conservación"],
          ["EDTA", "24 h a 4°C"],
          ["Heparina", "3-24 h según uso"],
          ["Citrato", "4-8 h a 4°C"],
          ["Gel separador", "8 h TA / 48 h refrigerado / 6 sem -20°C"]
        ]),
        ("Orden de extracción de tubos", "flow", [
          "1️⃣ Hemocultivos aeróbicos",
          "2️⃣ Hemocultivos anaeróbicos",
          "3️⃣ Tubo sin aditivos (tubo seco o gel separador, tapa roja/amarilla)",
          "4️⃣ Tubos con aditivos (citrato, heparina, EDTA, fluoruro)"
        ])
      ]),
      sec("4.4", "Interferencias en las muestras de sangre", [
        ("Principales interferencias", "grid", [
          ("Hemólisis", "Ruptura de glóbulos rojos. Hemoglobina >0,3 g/L. Altera valores, generalmente los aumenta o falsea"),
          ("Lipemia", "Exceso de lípidos por falta de ayuno. Afecta determinación de varios analitos"),
          ("Ictericia", "Exceso de bilirrubina. Plasma/suero amarillo intenso. >35 µmol/L hiperbilirrubinemia, >100 µmol/L ictericia"),
          ("Fármacos y drogas", "Alcohol, tabaco, medicamentos. Alteran resultados analíticos")
        ])
      ]),
      sec("4.5", "Obtención de plasma y suero", [
        ("Obtención de plasma", "flow", [
          "1️⃣ Centrifugación a 1300-1500 g durante 10 min → Diferenciación de fracciones",
          "2️⃣ Separación de la fracción superior (Plasma + Plaquetas)",
          "3️⃣ Centrifugación a 2500 g durante 15 min → Separación de plaquetas",
          "4️⃣ Separar sobrenadante y colocarlo en tubos para análisis",
          "Conservación: refrigeración (4°C) o congelación a -80°C"
        ]),
        ("Obtención de suero", "flow", [
          "1️⃣ Dejar reposar 20-30 min para coagulación completa. NO agitar para evitar hemólisis",
          "2️⃣ Centrifugar a 850-1000 g → Separar suero del coágulo",
          "3️⃣ Separar sobrenadante y colocarlo en tubos para análisis",
          "Los tubos deben permanecer cerrados para evitar pérdidas de agua"
        ])
      ]),
      sec("4.6", "Componentes de la sangre y productos derivados", [
        ("Hemocomponentes vs Hemoderivados", "", [
          "Hemocomponentes: uso clínico directo, almacenados en bancos de sangre",
          "Hemoderivados: uso farmacéutico, médico o de investigación"
        ]),
        ("Derivados plaquetarios", "", [
          "PRFC: Plasma Rico en Factores de Crecimiento",
          "PRP: Plasma Rico en Plaquetas",
          "Lisado plaquetar"
        ])
      ])
    ]
  },
  {
    "code": "U5",
    "title": "Muestras de orina",
    "emoji": "💧",
    "desc": "Composición, tipos de muestra, obtención, procesamiento, análisis y sedimento urinario",
    "sections": [
      sec("5.1", "Características y composición de la orina", [
        ("Definición", "", [
          "Líquido resultante del metabolismo, secretado por los riñones tras procesar la sangre",
          "Sirve para eliminar toxinas y elementos de desecho"
        ]),
        ("Composición", "", [
          "Agua (95%)",
          "Sales minerales (2%)",
          "Urea y ácido úrico (3%)",
          "Otros compuestos (<1%): cloruros, amonio, hormonas, creatinina"
        ])
      ]),
      sec("5.2", "Orina de una micción (espontánea)", [
        ("Obtención", "", [
          "Higiene genital previa antes de recoger la muestra",
          "Descartar el primer chorro",
          "Recoger la porción media en recipiente estéril",
          "Cerrar bien el envase y llevar al laboratorio antes de 2 horas",
          "Si tarda >2h: refrigerar a 4°C para evitar proliferación bacteriana"
        ]),
        ("Procesamiento", "flow", [
          "1️⃣ Recepción y verificación de datos",
          "2️⃣ Examen macroscópico",
          "3️⃣ Análisis bioquímico (tira reactiva)",
          "4️⃣ Sedimento urinario (centrifugación)",
          "5️⃣ Urocultivo (si procede)"
        ]),
        ("Sedimento urinario", "", [
          "Se obtiene por centrifugación de la orina",
          "Permite observar elementos formes: células, bacterias, cristales, cilindros",
          "Valora presencia de bacterias, leucocitos, hematíes, células epiteliales"
        ])
      ]),
      sec("5.3", "Orina de 24 horas", [
        ("Obtención", "", [
          "Recoger toda la orina excretada durante 24 horas consecutivas",
          "La primera micción del día se DESCARTA y se anota la hora",
          "A partir de ahí, toda la orina se recoge en el recipiente",
          "A las 24h, la última micción se añade al recipiente"
        ]),
        ("Procesamiento", "", [
          "Homogeneizar el contenido si se usan varios recipientes",
          "Medir volumen total",
          "Tomar alícuota para análisis"
        ]),
        ("Conservantes según análisis", "", [
          "Catecolaminas: Ácido clorhídrico 6N",
          "Proteinuria: sin conservante especial",
          "NO sirve para urocultivo (los conservantes inhiben bacterias)"
        ]),
        ("Errores comunes", "", [
          "Olvidar una micción invalida la prueba (pérdida de solutos totales)",
          "No homogeneizar antes de tomar la alícuota",
          "Usar recipiente no estéril"
        ])
      ]),
      sec("5.4", "Otros métodos de obtención de orina", [
        ("Sondaje vesical", "", [
          "La muestra debe obtenerse del puerto de punción de la sonda",
          "NUNCA de la bolsa colectora (alto riesgo de contaminación)",
          "Idealmente cambiar la sonda antes del cultivo si lleva mucho tiempo"
        ]),
        ("Volúmenes necesarios para cultivo", "", [
          "Bacterias: 0,5-1 mL",
          "Hongos: >20 mL",
          "Micobacterias: >20 mL"
        ])
      ]),
      sec("5.5", "Análisis de orina", [
        ("Tipos de análisis", "table", [
          ["Análisis", "Qué evalúa", "Objetivo"],
          ["Examen macroscópico", "Color, aspecto, olor, turbidez", "Detectar alteraciones visibles (ITU: orina turbia, color verdoso, olor fuerte)"],
          ["Análisis bioquímico", "pH, glucosa, proteínas, nitritos, cetonas, densidad", "Tira reactiva: resultados cualitativos/semicuantitativos"],
          ["Sedimento urinario", "Células, bacterias, cristales, cilindros", "Detectar infección, inflamación, patología renal"],
          ["Urocultivo", "Microorganismos (bacterias, hongos)", "Diagnóstico de infección urinaria con antibiograma"],
          ["Citopatología", "Células de la orina", "Detección de cáncer o alteraciones celulares"]
        ]),
        ("Citología urinaria", "", [
          "Muestra recomendada: micción de media mañana (no primera del día, tiene poca celularidad)",
          "Centrifugar para concentrar células",
          "Tinción más habitual: Papanicolau",
          "Alteraciones en tumoración: aumento nuclear, irregularidades de membrana, hipercromasia"
        ])
      ])
    ]
  },
  {
    "code": "U6",
    "title": "Muestras de obtención directa",
    "emoji": "🫁",
    "desc": "Esputo, heces y semen: obtención, procesamiento, análisis y aplicaciones clínicas",
    "sections": [
      sec("6.1", "Esputo", [
        ("Definición", "", [
          "Líquido segregado por los epitelios de los pulmones, textura mucosa entre líquida y sólida",
          "Útil para determinar el origen de enfermedades respiratorias"
        ]),
        ("Métodos de obtención", "table", [
          ["Método", "Procedimiento", "Ventajas", "Uso principal"],
          ["Expectoración espontánea", "Tos natural, recogida en bote", "Fácil, no invasivo", "Diagnóstico inicial"],
          ["Expectoración postural", "Paciente boca abajo, respiración profunda", "Ayuda si dificultad para expectorar", "Situaciones de expectoración difícil"],
          ["Expectoración inducida", "Inhalación de aerosoles hipertónicos", "Más controlado", "Pacientes con tos insuficiente"],
          ["Lavado broncoalveolar (BAL)", "100-200 mL líquido por broncoscopia", "Muestra de bronquiolos y alveolos", "Microbiología profunda, citología"],
          ["PAAF pulmonar", "Aguja atraviesa tejido pulmonar", "Alta calidad, mínima contaminación", "Diagnóstico preciso de lesiones"]
        ]),
        ("Preparación del paciente", "", [
          "Ayunas",
          "Enjuague con colutorio previamente para evitar contaminación bucal"
        ]),
        ("Análisis de esputos", "table", [
          ["Análisis", "Qué evalúa", "Objetivo"],
          ["Macroscópico", "Aspecto general, color, olor, consistencia", "En personas sanas: claro, acuoso e inodoro. Amarillento/verdoso = infección"],
          ["Citológico", "Tipo, morfología y alteraciones celulares", "Detectar infecciones, inflamación o neoplasias. Células cilíndricas = vías profundas"],
          ["Microbiológico", "Microorganismos patógenos", "S. pneumoniae, H. influenzae, M. tuberculosis (Ziehl-Neelsen)"],
          ["Recuento celular", "Cantidad de tipos celulares", "Eosinófilos elevados = alergia. Macrófagos/neutrófilos = infección"]
        ])
      ]),
      sec("6.2", "Heces", [
        ("Definición", "", [
          "Mezcla de sustancias y microorganismos formada en el intestino grueso a partir de los restos de la digestión"
        ]),
        ("Preparación del paciente según análisis", "table", [
          ["Análisis", "Dieta/Preparación", "Nº muestras", "Conservación"],
          ["Sangre oculta", "Evitar carne, embutidos, pescado, lentejas, espinacas, plátanos", "3 (días distintos)", "Cada muestra en frasco individual"],
          ["Principios inmediatos", "Sin dieta especial. Suspender bismuto, supositorios", "1", "Normal"],
          ["Parásitos", "Restringir medicamentos, papilla de bario, verduras, legumbres, frutas", "3 (días distintos)", "Temperatura ambiente. NO refrigerar"]
        ]),
        ("Pruebas y análisis de heces", "table", [
          ["Análisis", "Qué evalúa", "Objetivo"],
          ["Examen macroscópico", "Consistencia, color, olor, moco, sangre, restos", "Orientativo. Heces líquidas/mucosas = posible infección bacteriana"],
          ["Estudio químico", "pH (6,5-6,9), azúcares reductores, sangre oculta, grasas", "Intolerancias, detección sangre no visible"],
          ["Examen microscópico", "Fibras musculares, grasas (tinción Negro Sudán), almidón, cristales", "Identificar alteraciones. Cristales de Charcot-Leyden = alergia intestinal"],
          ["Coprocultivo", "Patógenos bacterianos", "Identificar bacteria causante de infección"]
        ])
      ]),
      sec("6.3", "Semen", [
        ("Obtención y condiciones", "", [
          "Abstinencia: entre 72 horas y 7 días",
          "Método: eyaculación directa en bote estéril o preservativo SIN espermicida",
          "Los preservativos normales contienen espermicidas que dañan espermatozoides",
          "Tiempo máximo hasta análisis: 2 horas",
          "Temperatura de transporte: corporal, evitando frío/calor y luz directa",
          "Licuefacción: paso de coagulado a líquido en 10-20 min (imprescindible antes de analizar)"
        ]),
        ("Análisis de semen (seminograma)", "table", [
          ["Análisis", "Qué evalúa", "Valores normales (OMS)"],
          ["Examen macroscópico", "Color, consistencia, licuefacción", "Color blanco opalescente. Pardo = sangre/inflamación"],
          ["Movilidad espermática", "Clasificación A-D", "A+B >50% o A ≥25%"],
          ["Concentración espermática", "Nº espermatozoides/mL", "≥15 millones/mL. <15 = oligozoospermia. 0 = azoospermia"],
          ["Morfología espermática", "Forma de espermatozoides", "≥4% normales (OMS), hasta 14% (criterios estrictos)"],
          ["Agregación/aglutinación", "Acumulaciones entre espermatozoides", "Alta concentración = posible infertilidad"]
        ]),
        ("Cultivo de semen", "", [
          "Detección de patógenos que causan infertilidad",
          "Se realiza junto con cultivos de orina, secreción prostática o frotis uretral"
        ])
      ])
    ]
  },
  {
    "code": "U7",
    "title": "Muestras procedentes de líquidos biológicos",
    "emoji": "🩻",
    "desc": "Líquido cefalorraquídeo, líquidos serosos (pleural, peritoneal, pericárdico) y líquido sinovial",
    "sections": [
      sec("7.1", "Líquido cefalorraquídeo (LCR)", [
        ("Definición", "", [
          "Líquido que se encuentra en el cráneo, entre la aracnoides y la piamadre",
          "Embebe el encéfalo y la médula espinal",
          "El tejido nervioso intercambia sustancias (nutrientes y desechos) a través del LCR"
        ]),
        ("Obtención", "", [
          "Método: punción percutánea lumbar",
          "Inserción de aguja en espacio intervertebral L3-L4 o L4-L5",
          "Procedimiento estéril y con anestesia local",
          "Se recogen 3-4 tubos para diferentes análisis"
        ]),
        ("Procesamiento y conservación", "", [
          "Procesar inmediatamente (las células se degradan rápido)",
          "Centrifugar para separar células del sobrenadante",
          "Conservar a 4°C si no se analiza de inmediato",
          "Congelar a -20°C o -80°C para análisis posteriores"
        ]),
        ("Análisis del LCR", "", [
          "Examen físico: aspecto, color, presión",
          "Recuento celular: leucocitos, hematíes",
          "Bioquímico: glucosa, proteínas, lactato",
          "Microbiológico: Gram, cultivo, antigenuria",
          "Normal: LCR claro e incoloro. Turbio = infección/meningitis"
        ])
      ]),
      sec("7.2", "Líquidos serosos", [
        ("Tipos de líquidos serosos", "table", [
          ["Líquido", "Localización", "Obtención", "Uso diagnóstico"],
          ["Líquido pleural", "Entre pleura parietal y visceral (pulmones)", "Toracocentesis", "Derrame pleural, infecciones, neoplasias"],
          ["Líquido peritoneal (ascítico)", "Cavidad abdominal", "Paracentesis", "Ascitis, peritonitis, neoplasias abdominales"],
          ["Líquido pericárdico", "Saco pericárdico (corazón)", "Pericardiocentesis", "Pericarditis, derrame pericárdico"]
        ]),
        ("Procesamiento general", "", [
          "Centrifugar para separar células",
          "Analizar sobrenadante para bioquímica",
          "Cultivo microbiológico si se sospecha infección",
          "Citología para detección de células neoplásicas",
          "Clasificar como trasudado o exudado (según proteinas/LDH)"
        ])
      ]),
      sec("7.3", "Líquido sinovial (LISI)", [
        ("Definición", "", [
          "Líquido viscoso que lubrica las articulaciones",
          "Compuesto por ácido hialurónico, proteínas y células",
          "Frecuente para estudio de artropatías"
        ]),
        ("Obtención", "", [
          "Método: artrocentesis (punción articular)",
          "Procedimiento estéril",
          "Se extrae por aspiración con aguja"
        ]),
        ("Análisis del líquido sinovial", "", [
          "Examen físico: color, viscosidad, claridad",
          "Recuento celular: leucocitos (polimorfonucleares vs mononucleares)",
          "Cristales: urato monosódico (gota), pirofosfato cálcico (pseudogota)",
          "Microbiológico: Gram, cultivo",
          "Bioquímico: glucosa, proteínas"
        ])
      ])
    ]
  },
  {
    "code": "U8",
    "title": "Exudados y muestras especiales",
    "emoji": "🔬",
    "desc": "Exudados genitourinarios, conjuntivales, óticos, micosis cutáneas y muestras especiales (líquido amniótico, médula ósea, citología digestiva)",
    "sections": [
      sec("8.1", "Exudados: concepto y tipos", [
        ("Definición", "", [
          "Elementos extravasados en el proceso inflamatorio",
          "Se depositan en el intersticio de los tejidos o cavidades del organismo",
          "Indican procesos inflamatorios o infecciosos"
        ]),
        ("Obtención y transporte general", "", [
          "Recoger con hisopo estéril de la zona afectada",
          "Transportar en medio de cultivo específico (Stuart, Amies)",
          "Conservar a temperatura ambiente",
          "Procesar en menos de 2 horas o refrigerar"
        ]),
        ("Tipos de exudados", "grid", [
          ("Exudados genitourinarios", "Muestras de genitales, frecuentes en infecciones de cierta magnitud. Procesamiento: tinción Gram + cultivo en medios específicos"),
          ("Exudados conjuntivales y corneales", "Raspado conjuntival o corneal con hisopo. Cultivo para bacterias y hongos. Tinción Gram y Giemsa"),
          ("Exudados óticos", "Muestra del conducto auditivo externo. Frecuente en otitis. Cultivo bacteriano y fúngico"),
          ("Exudados de úlceras y heridas", "Hisopo de la zona más profunda de la herida. Cultivo aeróbico y anaeróbico")
        ])
      ]),
      sec("8.2", "Micosis cutáneas", [
        ("Obtención de muestras", "", [
          "Raspado de escamas de la piel con bisturí estéril",
          "Recortes de uñas afectadas",
          "Cabellos con raíz para infecciones del cuero cabelludo"
        ]),
        ("Conservación y transporte", "", [
          "Colocar en recipiente estéril seco",
          "NO refrigerar (los hongos se ven afectados por el frío)",
          "Procesar en menos de 24 horas"
        ])
      ]),
      sec("8.3", "Muestras especiales", [
        ("Líquido amniótico", "", [
          "Obtenido por amniocentesis (semana 15-17)",
          "Uso: diagnóstico prenatal de anomalías genéticas",
          "Procesamiento: cultivo celular para cariotipo",
          "También: análisis de alfafetoproteína, bilirrubina"
        ]),
        ("Médula ósea", "", [
          "Obtención por aspiración (esternón o cresta ilíaca)",
          "Uso: diagnóstico de leucemias, linfomas, mieloma",
          "Procesamiento: extensión en portaobjetos, tinción",
          "También para cultivo y citogenética"
        ]),
        ("Citología exfoliativa del aparato digestivo", "", [
          "Obtención por cepillado endoscópico o lavado",
          "Zonas: esófago, estómago, colon",
          "Tinción: Papanicolau, Hematoxilina-Eosina",
          "Uso: detección de lesiones premalignas y neoplasias"
        ])
      ])
    ]
  },
  {
    "code": "U9",
    "title": "Muestras de anatomía patológica y citodiagnóstico",
    "emoji": "🧬",
    "desc": "Histología vs citopatología, biopsias, piezas quirúrgicas, procesamiento de tejidos y muestras citológicas",
    "sections": [
      sec("9.1", "Histología y citopatología", [
        ("Definiciones", "", [
          "Histología: estudio general de los tejidos biológicos del cuerpo humano",
          "Citopatología: ciencia que estudia alteraciones morfológicas de células desprendidas de tejidos"
        ]),
        ("Diferencias principales", "table", [
          ["Aspecto", "Histología", "Citopatología"],
          ["Objeto de estudio", "Tejidos (conjuntos de células organizadas)", "Células individuales o grupos pequeños"],
          ["Obtención", "Biopsias, piezas quirúrgicas", "Impronta, PAAF, raspado"],
          ["Procesamiento", "Fijación → Inclusión → Corte → Tinción", "Extensión → Fijación → Tinción"],
          ["Información", "Arquitectura tisular y relaciones celulares", "Morfología celular individual"]
        ])
      ]),
      sec("9.2", "Biopsias", [
        ("Tipos de biopsias", "table", [
          ["Tipo", "Descripción", "Indicaciones"],
          ["Biopsia incisional", "Extirpación quirúrgica de una pequeña porción de la lesión", "Lesiones grandes donde no se puede extirpar todo"],
          ["Biopsia escisional", "Extirpación completa de toda la lesión", "Lesiones pequeñas potencialmente curables"],
          ["Biopsia con aguja gruesa", "Obtención de cilindro de tejido con aguja especial", "Tumores profundos (mama, próstata, hígado)"]
        ]),
        ("Piezas quirúrgicas", "", [
          "Órganos completos o partes de ellos extirpados en cirugía",
          "Requieren orientación anatómica por parte del cirujano",
          "Se marcan con tinta de India para orientación histológica",
          "Procesamiento completo para diagnóstico definitivo"
        ])
      ]),
      sec("9.3", "Procesamiento de muestras de tejidos", [
        ("Fijación", "", [
          "Preserva la morfología del tejido evitando autólisis y putrefacción",
          "Fijador más común: formol tamponado al 10% (formaldehído 4%)",
          "Tiempo de fijación: 24-48 h a temperatura ambiente",
          "Volumen: 10-20 veces el volumen del tejido"
        ]),
        ("Inclusión", "flow", [
          "1️⃣ Deshidratación en alcoholes de concentración creciente (70% → 96% → 100%)",
          "2️⃣ Aclaramiento en xileno (elimina el alcohol)",
          "3️⃣ Infiltración en parafina líquida en estufa a 60°C",
          "4️⃣ Inclusión en bloque de parafina (orientación del tejido)"
        ]),
        ("Corte (microtomía)", "", [
          "Microtomo: equipo para cortar secciones finas del bloque de parafina",
          "Grosor habitual: 3-5 micrómetros",
          "Las secciones se colocan en baño de flotación (agua tibia 40-45°C)",
          "Se recogen en portaobjetos para tinción"
        ]),
        ("Tinción", "", [
          "Hematoxilina-Eosina (H&E): tinción de rutina más común",
          "Hematoxilina: tiñe núcleos (azul/violeta)",
          "Eosina: tiñe citoplasma y matriz extracelular (rosa)",
          "Otras tinciones: Tricrómico, PAS, Reticulina, Inmunohistoquímica"
        ])
      ]),
      sec("9.4", "Muestras citológicas", [
        ("Impronta citológica", "", [
          "Presionar suavemente el tejido fresco contra un portaobjetos",
          "Las células se adhieren al vidrio",
          "Rápido, útil para diagnóstico intraoperatorio",
          "Tinción: Diff-Quik o Papanicolau"
        ]),
        ("PAAF (Punción Aspiración con Aguja Fina)", "", [
          "Inserción de aguja fina (22-25G) en la lesión",
          "Aspiración con presión negativa",
          "Zonas: tiroides, mama, ganglios, partes blandas",
          "Extensión del material en portaobjetos",
          "Fijación y tinción (Papanicolau, Diff-Quik)"
        ]),
        ("Procesamiento de citologías", "flow", [
          "1️⃣ Extensión de la muestra en portaobjetos",
          "2️⃣ Fijación inmediata (alcohol 96% o citospray)",
          "3️⃣ Tinción (Papanicolau, H&E, Diff-Quik)",
          "4️⃣ Montaje con cubreobjetos y resina",
          "5️⃣ Observación al microscopio y diagnóstico"
        ])
      ])
    ]
  },
  {
    "code": "U10",
    "title": "Muestras de biobancos y animales de experimentación",
    "emoji": "🧊",
    "desc": "Biobancos, procesamiento y conservación de muestras, marco ético-jurídico y animales de laboratorio",
    "sections": [
      sec("10.1", "Concepto y características de los biobancos", [
        ("Definición", "", [
          "Instalaciones donde se almacenan muestras biológicas con fines de investigación",
          "Reservas de material biológico para uso futuro en tratamientos"
        ]),
        ("Origen y funciones", "", [
          "Registro del material donado voluntariamente",
          "Registro de material no recogido o gestionado para investigación",
          "Destino de los excedentes",
          "Fines: investigación, tratamientos futuros"
        ])
      ]),
      sec("10.2", "Obtención y preparación de muestras", [
        ("Tumores y tejidos sanos", "", [
          "Procedentes de cirugías (piezas quirúrgicas)",
          "Tejido tumoral y tejido sano adyacente (control)",
          "Procesamiento inmediato tras la extirpación"
        ]),
        ("Fluidos y células", "", [
          "Sangre, plasma, suero, orina, LCR",
          "Células ex vivo: proceden directamente de tejidos de personas",
          "Importante: conservar la viabilidad celular"
        ])
      ]),
      sec("10.3", "Procesamiento de muestras", [
        ("Tejidos y tumores", "", [
          "Fragmentaci ón en porciones pequeñas",
          "Congelación rápida en nitrógeno líquido (-196°C)",
          "Inclusión en parafina para estudios histológicos"
        ]),
        ("ADN y ARN", "", [
          "Extracción con kits específicos",
          "Conservación a -80°C",
          "Evaluación de calidad (A260/A280, integridad)"
        ]),
        ("Células", "", [
          "Criopreservación en medio con DMSO al 10%",
          "Congelación gradual (-1°C/min)",
          "Almacenamiento en nitrógeno líquido"
        ]),
        ("Fluidos", "", [
          "Centrifugación para separar componentes",
          "Alicuotado para evitar ciclos de congelación-descongelación",
          "Almacenamiento a -80°C"
        ])
      ]),
      sec("10.4", "Conservación y transporte de muestras", [
        ("Métodos de conservación", "table", [
          ["Método", "Temperatura", "Tipo de muestra", "Duración"],
          ["Refrigeración", "4°C", "Fluidos, tejidos frescos", "Corto plazo (días)"],
          ["Congelación", "-20°C", "Plasma, suero", "Medio plazo (meses)"],
          ["Ultracongelación", "-80°C", "ADN, ARN, tejidos", "Largo plazo (años)"],
          ["Nitrógeno líquido", "-196°C", "Células, tejidos viables", "Indefinido"]
        ]),
        ("Transporte", "", [
          "Cadena de frío: mantener temperatura constante",
          "Contenedores isotérmicos con hielo seco o packs refrigerantes",
          "Identificación clara de cada muestra",
          "Documentación de trazabilidad",
          "Cumplir normativa de transporte de muestras biológicas"
        ])
      ]),
      sec("10.5", "Marco ético y jurídico", [
        ("Aspectos éticos", "", [
          "Consentimiento informado del donante",
          "Confidencialidad de datos (anonimización)",
          "Uso exclusivo para fines de investigación autorizados"
        ]),
        ("Legislación aplicable", "", [
          "Ley de Investigación Biomédica",
          "Reglamento de Biobancos",
          "LOPD y Reglamento General de Protección de Datos (RGPD)"
        ])
      ]),
      sec("10.6", "Animales de laboratorio", [
        ("Principales tipos", "grid", [
          ("Roedores", "Ratones y ratas: los más usados en investigación biomédica. Genéticamente modificables, ciclo reproductivo corto"),
          ("Conejos", "Usados en inmunología, producción de anticuerpos y pruebas de irritación"),
          ("Peces cebra", "Modelo vertebrado para genética del desarrollo, toxicología"),
          ("Primates no humanos", "Modelos más cercanos al humano. Uso restringido por cuestiones éticas")
        ]),
        ("Manipulación y bienestar", "", [
          "Alojamiento en condiciones controladas (temperatura, humedad, ciclo luz/oscuridad)",
          "Alimentación y agua ad libitum",
          "Enriquecimiento ambiental",
          "Personal entrenado y cualificado"
        ]),
        ("Aspectos éticos y legislación", "", [
          "Principio de las 3Rs: Reemplazar, Reducir, Refinar",
          "Directiva 2010/63/UE de protección de animales utilizados para fines científicos",
          "Real Decreto 53/2013 en España",
          "Comité de Ética de Experimentación Animal: aprueba todos los protocolos"
        ])
      ])
    ]
  }
]

# Key points for each unit
key_points = {
    "U1": [
        "Sistema sanitario = instituciones + personal + normas + medios para asistencia sanitaria",
        "SNS español: Universalidad, Atención integrada, Participación, Financiación, Eficacia",
        "Organización: Nivel central (Ministerio) → Autonómico (Consejería) → Área de Salud",
        "Atención Primaria (centros de salud) vs Especializada (hospitales)",
        "Core Lab: laboratorio central automatizado que optimiza recursos y reduce costes",
        "Fases: Preanalítica (toma/transporte) → Analítica (análisis) → Postanalítica (informe)",
        "Funciones del técnico: toma de muestras, análisis, gestión de existencias y residuos"
    ],
    "U2": [
        "Flujo: Recepción → Registro → Clasificación → Procesamiento → Análisis → Validación → Informe",
        "Trazabilidad: sistema que permite identificar y ubicar muestras en cualquier etapa",
        "SIL: Sistemas de Información del Laboratorio (registrar, procesar, almacenar, consultar)",
        "LOPD: protege datos de salud. Consentimiento informado: voluntario, revocable",
        "FIFO (First In, First Out): sistema de almacén más usado en sanidad para evitar caducidades",
        "Albarán: prueba de entrega de mercancía",
        "Material fungible (desechable) vs no fungible (reutilizable)"
    ],
    "U3": [
        "Muestras biológicas: porciones de organismos vivos para análisis",
        "Líquidas corporales (información general) vs Secreciones (función órganos) vs Exudados (inflamación)",
        "Citología descamativa (raspado) vs aspirativa (PAAF con aguja)",
        "Análisis cualitativo (qué hay) vs cuantitativo (cuánto hay)",
        "Variabilidad preanalítica: edad, sexo, dieta, ejercicio, fármacos, hemólisis, lipemia",
        "PSA: marcador específico de cáncer de próstata en hombres",
        "Errores preanalíticos: muestra mal etiquetada, contaminación, ayuno incumplido"
    ],
    "U4": [
        "Extracción venosa: retirar torniquete ANTES de retirar aguja",
        "Extracción arterial: gasometría. Capilar: niños, poco volumen",
        "Hemocultivos: aeróbicos (con O₂) y anaeróbicos (sin O₂)",
        "Orden de tubos: Hemocultivos → Tubo seco → Tubos con aditivos",
        "EDTA (hematología), Citrato (coagulación), Heparina (bioquímica)",
        "Hemólisis (rótura GR), Lipemia (lípidos), Ictericia (bilirrubina): interferencias",
        "Plasma: centrifugación inicial a 1300-1500g. Suero: reposo 20-30 min + centrífuga 850-1000g"
    ],
    "U5": [
        "Composición orina: 95% agua, 2% sales, 3% urea/ácido úrico",
        "Micción espontánea: higiene → descartar primer chorro → porción media → <2h laboratorio",
        "Orina 24h: descartar primera micción, recoger todo, homogeneizar",
        "Orina de sonda: puerto de punción, NUNCA bolsa colectora",
        "Urocultivo: porción media sin conservantes (inhiben bacterias)",
        "Sedimento: centrifugación para ver células, bacterias, cristales, cilindros",
        "Citología urinaria: micción media mañana, tinción Papanicolau"
    ],
    "U6": [
        "Esputo: expectoración espontánea (inicial) → inducida (aerosoles) → BAL (broncoscopia)",
        "Lavado broncoalveolar (BAL): 100-200 mL para microbiología profunda",
        "Esputo verdoso/amarillento = infección. Células cilíndricas = vías profundas",
        "Heces: 3 muestras días distintos para parásitos. NO refrigerar",
        "Tinción Negro Sudán para grasas en heces",
        "Semen: abstinencia 72h-7días, licuefacción 10-20 min, análisis <2h",
        "Seminograma: concentración ≥15 mill/mL, movilidad A+B >50%, morfología ≥4% normal"
    ],
    "U7": [
        "LCR: punción lumbar L3-L4 o L4-L5. LCR claro = normal. Turbio = meningitis",
        "Líquidos serosos: pleural (toracocentesis), peritoneal (paracentesis), pericárdico (pericardiocentesis)",
        "Clasificar derrames: trasudado vs exudado (proteinas/LDH)",
        "Líquido sinovial: artrocentesis. Cristales: urato (gota), pirofosfato (pseudogota)",
        "Procesar LCR inmediatamente (células se degradan rápido)",
        "Citología de líquidos: detección de células neoplásicas"
    ],
    "U8": [
        "Exudados: elementos extravasados en proceso inflamatorio",
        "Transporte en medio Stuart/Amies, procesar <2h",
        "Exudados genitourinarios: Gram + cultivo en medios específicos",
        "Micosis cutáneas: raspado de escamas. NO refrigerar (hongos sensibles al frío)",
        "Líquido amniótico: amniocentesis semana 15-17, diagnóstico prenatal",
        "Médula ósea: aspiración de esternón/cresta ilíaca para leucemias, linfomas",
        "Citología digestiva exfoliativa: cepillado endoscópico, tinción Papanicolau"
    ],
    "U9": [
        "Histología: estudia tejidos. Citopatología: estudia células individuales",
        "Biopsia incisional (porción) vs escisional (completa) vs aguja gruesa (cilindro)",
        "Procesamiento tejidos: Fijación (formol 10%) → Inclusión (parafina) → Corte (3-5µm) → Tinción (H&E)",
        "Hematoxilina: núcleos azules. Eosina: citoplasma rosa",
        "PAAF: aguja fina 22-25G, aspiración con presión negativa",
        "Impronta: presionar tejido fresco contra portaobjetos, rápido intraoperatorio",
        "Citología: extensión → fijación inmediata (alcohol 96%) → tinción → montaje"
    ],
    "U10": [
        "Biobancos: instalaciones para almacenar muestras biológicas con fines de investigación",
        "Células ex vivo: proceden directamente de tejidos de personas",
        "Conservación: 4°C (días) → -20°C (meses) → -80°C (años) → N₂ líquido -196°C (indefinido)",
        "Criopreservación celular: DMSO 10%, congelación gradual -1°C/min",
        "Transporte: cadena de frío constante, contenedores isotérmicos, trazabilidad",
        "Principio 3Rs en animales: Reemplazar, Reducir, Refinar",
        "Directiva 2010/63/UE y RD 53/2013: legislación sobre experimentación animal"
    ]
}

# ============= HTML generation =============

total_units = len(units)

html = '''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Gestión de Muestras Biológicas — Guía Interactiva</title>
<style>
:root{--bg:#0a0f1f;--card:#111827;--card2:#1a2332;--a:#00d4aa;--a2:#7c5bf0;--t:#e8ecf5;--t2:#8892b0;--b:#4a9eff;--y:#f5c842;--o:#ff9f43;--r:#ff6b6b}
*{margin:0;padding:0;box-sizing:border-box;scroll-behavior:smooth}
body{font-family:'Segoe UI',system-ui,sans-serif;background:var(--bg);color:var(--t);min-height:100vh}
::selection{background:rgba(0,212,170,.25)}
.topbar{background:linear-gradient(135deg,#0a1025,#14203a);padding:12px 20px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid rgba(255,255,255,.06);position:sticky;top:0;z-index:100;flex-wrap:wrap;gap:8px}
.topbar h1{font-size:17px;font-weight:800;background:linear-gradient(135deg,var(--a),#48dbfb);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.topbar .sub{font-size:10px;color:var(--t2);-webkit-text-fill-color:var(--t2)}
.searchbox{background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.08);border-radius:8px;padding:8px 12px;color:var(--t);width:200px;font-size:12px;outline:none;transition:.3s}
.searchbox:focus{border-color:var(--a);background:rgba(0,212,170,.05);width:240px}
.searchbox::placeholder{color:var(--t2);opacity:.6}
.nav{display:flex;gap:5px;padding:10px 20px;background:rgba(10,14,26,.95);border-bottom:1px solid rgba(255,255,255,.04);position:sticky;top:47px;z-index:99;overflow-x:auto}
.nav-btn{padding:6px 14px;border-radius:8px;border:none;cursor:pointer;font-weight:600;font-size:11px;transition:.2s;background:var(--card);color:var(--t2);white-space:nowrap;flex-shrink:0}
.nav-btn:hover{background:var(--card2);transform:translateY(-1px)}
.nav-btn.active{background:linear-gradient(135deg,var(--a),#00b894);color:#0a0e1a;box-shadow:0 2px 12px rgba(0,212,170,.2)}
.main{max-width:1000px;margin:0 auto;padding:14px 18px 50px}
.unit{display:none;animation:fadeIn .3s}
.unit.active{display:block}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
.hero{background:linear-gradient(135deg,var(--card),#0e1729);border-radius:12px;padding:20px 24px;margin-bottom:14px;border:1px solid rgba(255,255,255,.05)}
.hero h2{font-size:18px;font-weight:700;margin-bottom:5px}
.hero h2 .c{color:var(--a)}
.hero p{color:var(--t2);font-size:12px}
.badges{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px}
.badge{padding:3px 9px;border-radius:5px;font-size:10px;font-weight:500}
.b1{background:rgba(0,212,170,.12);color:var(--a)}
.b2{background:rgba(74,158,255,.12);color:var(--b)}
.b3{background:rgba(124,91,240,.12);color:var(--a2)}
.secc{background:var(--card);border-radius:12px;margin-bottom:10px;border:1px solid rgba(255,255,255,.04);overflow:hidden}
.sech{display:flex;align-items:center;gap:8px;padding:12px 16px;cursor:pointer;user-select:none;transition:.15s;font-size:13px;font-weight:600}
.sech:hover{background:rgba(255,255,255,.02)}
.sech .arrow{font-size:10px;transition:.2s;width:16px;text-align:center;color:var(--a);flex-shrink:0}
.sech .arrow.o{transform:rotate(90deg)}
.sech .num{color:var(--a);font-weight:700;min-width:30px;font-size:12px}
.secb{display:none;padding:0 16px 14px;border-top:1px solid rgba(255,255,255,.04);padding-top:10px}
.secb.open{display:block}
.stitle{padding:6px 10px;font-size:12px;font-weight:600;color:var(--t);background:var(--card2);border-radius:6px;margin:8px 0 6px;display:flex;align-items:center;gap:6px;border-left:3px solid var(--a)}
.stitle.purple{border-left-color:var(--a2)}
.stitle.orange{border-left-color:var(--o)}
.cbody{padding:2px 6px}
.cbody p{font-size:12px;line-height:1.65;color:var(--t2);margin-bottom:6px}
.cbody ul{list-style:none;padding:0 4px}
.cbody ul li{font-size:12px;color:var(--t2);padding:3px 0 3px 18px;position:relative;line-height:1.5}
.cbody ul li::before{content:"\\25b8";position:absolute;left:2px;color:var(--a);font-weight:700}
.tbl{overflow-x:auto;margin:6px 0;border-radius:6px;font-size:11px}
.tbl table{width:100%;border-collapse:collapse}
.tbl th{background:var(--card2);color:var(--a);padding:6px 10px;text-align:left;font-weight:600;border-bottom:1px solid rgba(0,212,170,.15);white-space:nowrap;font-size:11px}
.tbl td{padding:5px 10px;border-bottom:1px solid rgba(255,255,255,.04);color:var(--t2);vertical-align:top}
.tbl tr:hover td{background:rgba(0,212,170,.03)}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin:6px 0}
.gitem{padding:8px 10px;background:var(--card2);border-radius:6px;border:1px solid rgba(255,255,255,.04)}
.gitem .gl{color:var(--a);font-size:11px;font-weight:600;margin-bottom:2px}
.gitem .gv{color:var(--t2);font-size:11px;line-height:1.4}
.dia{display:flex;flex-direction:column;gap:4px;padding:8px 0}
.dstep{display:flex;align-items:center;gap:8px;padding:6px 10px;background:var(--card2);border-radius:6px;font-size:11px;color:var(--t2)}
.dstep .arr{color:var(--a);font-weight:700;min-width:20px}
.dstep:not(:last-child){margin-bottom:2px}
.dstep.s{margin-left:20px;background:rgba(0,212,170,.04);border-left:2px solid var(--a)}
.pwrap{display:flex;align-items:center;gap:10px;padding:10px 16px;background:var(--card);border-radius:12px;border:1px solid rgba(255,255,255,.04);margin:14px 0 6px}
.pbar{flex:1;display:flex;gap:3px}
.pdot{height:4px;border-radius:2px;flex:1;background:var(--card2);transition:.3s}
.pdot.a{background:linear-gradient(90deg,var(--a),var(--b))}
.nava{display:flex;gap:5px}
.navb{width:28px;height:28px;border-radius:6px;border:1px solid rgba(255,255,255,.08);background:var(--card2);color:var(--t2);cursor:pointer;display:flex;align-items:center;justify-content:center;font-size:13px;transition:.15s}
.navb:hover{background:var(--a);color:#0a0e1a;border-color:var(--a)}
.st{position:fixed;bottom:20px;right:20px;width:36px;height:36px;border-radius:50%;background:var(--a);color:#0a0e1a;border:none;cursor:pointer;font-size:18px;opacity:0;transition:.3s;pointer-events:none;z-index:50;box-shadow:0 3px 12px rgba(0,212,170,.3)}
.st.v{opacity:1;pointer-events:auto}
@media(max-width:768px){
  .topbar{padding:10px 14px}.searchbox{width:100%}.searchbox:focus{width:100%}
  .nav{top:42px;padding:8px 12px}
  .main{padding:10px 12px}.hero{padding:14px 16px}.hero h2{font-size:15px}
  .secc{padding:0}.sech{padding:10px 12px;font-size:12px}
  .grid2{grid-template-columns:1fr}
}
.qans{padding:10px 14px;background:rgba(0,212,170,.1);border-left:3px solid var(--a);border-radius:0 6px 6px 0;font-size:13px;color:var(--a)!important;margin-top:4px}
</style>
</head>
<body>
<div class="topbar">
  <div><h1>🧬 Gestión de Muestras Biológicas</h1><div class="sub">Guía interactiva de estudio • 10 unidades</div></div>
  <input class="searchbox" id="s" placeholder="\\ud83d\\udd0d Buscar..." oninput="su(this.value)">
</div>
<div class="nav" id="nav">'''

# Navigation buttons
for ui, u in enumerate(units):
    short = u["title"][:40]
    if len(u["title"]) > 40:
        short += "…"
    act = " active" if ui == 0 else ""
    html += f'<button class="nav-btn{act}" onclick="x({ui})"><b>{u["code"]}</b> {short}</button>'

html += '</div><div class="main" id="m">'

# Unit content
for ui, u in enumerate(units):
    act = " active" if ui == 0 else ""
    html += f'<div class="unit{act}" id="u{ui}">\n'
    sec_count = len(u["sections"])
    topic_count = sum(len(s["content"]) for s in u["sections"])
    
    html += f'''<div class="hero"><h2>{u["emoji"]} <span class="c">{u["code"]}:</span> {u["title"]}</h2><p>{u["desc"]}</p>
<div class="badges"><span class="badge b1">📖 {sec_count} secciones</span>
<span class="badge b2">📄 {topic_count} temas</span>
<span class="badge b3">{u["emoji"]} {u["code"]}</span></div></div>\n'''

    for s in u["sections"]:
        html += f'<div class="secc">\n<div class="sech" onclick="tsec(this)"><span class="arrow">▶</span><span class="num">{s["num"]}</span>{s["title"]}</div>\n<div class="secb">\n'
        for item in s["content"]:
            title = item[0]
            kind = item[1] if len(item) > 1 else ""
            data = item[2] if len(item) > 2 else []
            
            # Determine icon prefix for stitle
            if kind == "table":
                prefix = "📊"
            elif kind == "grid":
                prefix = "🔲"
            elif kind == "grid2":
                prefix = "📋"
            elif kind == "flow":
                prefix = "📌"
            else:
                prefix = ""
            
            html += f'<div class="stitle {"purple" if kind else ""}">{prefix} {title}</div>\n<div class="cbody">\n'
            
            if kind == "table":
                html += '<div class="tbl"><table>'
                if isinstance(data, list) and len(data) > 0:
                    for i, row in enumerate(data):
                        html += '<tr>'
                        for cell in row:
                            tag = "th" if i == 0 else "td"
                            html += f'<{tag}>{cell}</{tag}>'
                        html += '</tr>'
                html += '</tbody></table></div>'
            elif kind == "grid":
                html += '<div class="tbl"><table><tbody>'
                for row in data:
                    html += '<tr>'
                    if isinstance(row, str):
                        html += f'<td>{row}</td>'
                    else:
                        for cell in row:
                            html += f'<td>{cell}</td>'
                    html += '</tr>'
                html += '</tbody></table></div>'
            elif kind == "grid2":
                html += '<div class="grid2">'
                for item2 in data:
                    if isinstance(item2, tuple):
                        html += f'<div class="gitem"><div class="gl">{item2[0]}</div><div class="gv">{item2[1]}</div></div>'
                    else:
                        pass
                html += '</div>'
            elif kind == "flow":
                html += '<div class="dia">'
                for step in data:
                    html += f'<div class="dstep"><span class="arr">→</span>{step}</div>'
                html += '</div>'
            else:
                # list or paragraph
                if isinstance(data, list):
                    html += '<ul>'
                    for li in data:
                        html += f'<li>{li}</li>'
                    html += '</ul>'
                elif isinstance(data, str):
                    html += f'<p>{data}</p>'
            
            html += '</div>\n'
        html += '</div></div>\n'
    
    # Key points section
    kp_code = u["code"]
    if kp_code in key_points:
        html += f'''<div class="secc" style="border-left:3px solid var(--y)">
<div class="sech" onclick="tsec(this)"><span class="arrow">▶</span><span class="num">⭐</span> Puntos Clave</div>
<div class="secb"><div class="stitle orange">Lo más importante de {kp_code}</div><div class="cbody"><ul>\n'''
        for kp in key_points[kp_code]:
            html += f'<li style="font-size:12px;color:var(--y);font-weight:500">{kp}</li>\n'
        html += '</ul></div></div></div>\n'
    
    # Progress bar & navigation
    html += f'''<div class="pwrap">
<div class="pbar">'''
    for p in range(total_units):
        cl = 'a' if p <= ui else ''
        html += f'<div class="pdot {cl}"></div>'
    html += f'''</div><span style="font-size:10px;color:var(--t2)">{u["code"]}/{total_units}</span>
<div class="nava"><button class="navb" onclick="xma({ui-1},{total_units-1})">‹</button>
<button class="navb" onclick="xmi({ui+1},{total_units-1})">›</button></div></div></div>\n'''

# Close main
html += '''</div><button class="st" id="st" onclick="window.scrollTo({top:0,behavior:'smooth'})">↑</button>
<script>
let cu=0;
function x(i){let u=document.getElementById('u'+i);let b=document.querySelectorAll('.nav-btn');
  document.querySelectorAll('.unit').forEach(e=>e.classList.remove('active'));
  b.forEach(e=>e.classList.remove('active'));
  if(u)u.classList.add('active');if(b[i])b[i].classList.add('active');cu=i;window.scrollTo({top:0,behavior:'smooth'});
}
function xma(i,m){if(i>=0)x(i)}
function xmi(i,m){if(i<=m)x(i)}
function su(q){q=q.toLowerCase().trim();
  if(!q){x(cu);return;}
  document.querySelectorAll('.unit').forEach((u,i)=>{
    let m=u.textContent.toLowerCase().includes(q);
    u.classList.toggle('active',m);
    let b=document.querySelectorAll('.nav-btn');
    if(b[i])b[i].classList.toggle('active',m);
  });
}
function tsec(el){let b=el.nextElementSibling;if(!b)return;
  b.classList.toggle('open');
  el.querySelector('.arrow').classList.toggle('o',b.classList.contains('open'));
}
window.addEventListener('scroll',()=>{document.getElementById('st').classList.toggle('v',window.scrollY>300)});
document.addEventListener('keydown',e=>{
  if(e.target.tagName==='INPUT')return;
  if(e.key==='ArrowRight'||e.key==='ArrowDown'){e.preventDefault();x(Math.min(cu+1,9));}
  if(e.key==='ArrowLeft'||e.key==='ArrowUp'){e.preventDefault();x(Math.max(cu-1,0));}
});
let tx=0;
document.addEventListener('touchstart',e=>{tx=e.changedTouches[0].screenX});
document.addEventListener('touchend',e=>{
  if(e.target.tagName==='INPUT')return;
  let d=e.changedTouches[0].screenX-tx;
  if(Math.abs(d)>80)x(Math.max(0,Math.min(9,cu-(d>0?1:-1))));
});
</script>
</body>
</html>'''

# Write to file
output_path = '/home/jeikson/.openclaw/workspace/muestras-biologicas-guia/index.html'
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(html)

total_secs = sum(len(u["sections"]) for u in units)
total_topics = sum(sum(len(s["content"]) for s in u["sections"]) for u in units)
print(f'✅ HTML generado: {len(html):,} chars | {len(units)} unidades | {total_secs} secciones | {total_topics} temas')
print(f'📁 {output_path}')

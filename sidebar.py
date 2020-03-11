archivos = {"tutorial-videos/index.html": "Edición de Video",
            "tables.html": "Tablas", 
            "buttons.html": "Botones",
            "cards.html": "Cartas",
            "utilities-color.html": "Color", 
            "utilities-border.html": "Bordes", 
            "utilities-animation.html": "Animaciones",
            "utilities-other.html": "Otros",
            "404.html": "404",
            "blank.html": "En blanco",
            "charts.html": "Cartas"}

mapa = {"Difusión": {"tutorial-videos/index.html"},
    "Components": ["buttons.html", 
                "cards.html"], 
    "Utilities": ["utilities-color.html", 
                "utilities-border.html", 
                "utilities-animation.html",
                "utilities-other.html"],
    "Pages": ["404.html", 
            "blank.html"]}




head = """
<head>

  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>Cuerpo de Tutores Ingeniería UC</title>

  <!-- Custom fonts for this template-->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

  <!-- Custom styles for this template-->
  <link href="css/sb-admin-2.min.css" rel="stylesheet">
  <link href="css/estilo.css" rel="stylesheet">

</head>
"""

sidebar = """
    <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion toggled" id="accordionSidebar" style="background-color:var(--primary);background-image:var(--primary)" >

"""

sidebar_brand = """
      <a class="sidebar-brand d-flex align-items-center justify-content-center" href="index.html">
        <div class="sidebar-brand-icon" style="vertical-align:bottom"> <!--rotate-n-15-->
          <i class="icon-logo-tutoresinguc" style="font-size:2.8rem;vertical-align:bottom"></i>
        </div>
        <div class="sidebar-brand-text mx-3" style="line-height:1rem;vertical-align:bottom;font-size:0.8rem;text-align:left;font-family: 'Roboto Condensed', sans-serif;"><p style="padding:0;margin:0">Cuerpo</p> <p style="padding:0;margin:0">de</p> <p style="padding:0;margin:0">Tutores</p> <sup></sup></div>
      </a>

"""


barra = """
    <!-- Nav Item - Dashboard -->
      <li class="nav-item active">
        <a class="nav-link" href="index.html">
          <i class="fas fa-fw fa-tachometer-alt"></i>
          <span>Dashboard</span></a>
      </li>

      <!-- Divider -->
      <hr class="sidebar-divider">

      <!-- Heading -->
      <div class="sidebar-heading">
        Interface
      </div>

      <li class="nav-item">
        <a class="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="true" aria-controls="collapseTwo">
          <i class="fas fa-fw fa-cog"></i>
          <span>Difusión</span>
        </a>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionSidebar">
          <div class="bg-white py-2 collapse-inner rounded">
            <h6 class="collapse-header">Tutoriales:</h6>
            <a class="collapse-item" href="tutotial-videos/index.html">Edición de Video</a>
          </div>
        </div>
      </li>


      <!-- Nav Item - Pages Collapse Menu -->
      <li class="nav-item">
        <a class="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="true" aria-controls="collapseTwo">
          <i class="fas fa-fw fa-cog"></i>
          <span>Components</span>
        </a>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordionSidebar">
          <div class="bg-white py-2 collapse-inner rounded">
            <h6 class="collapse-header">Custom Components:</h6>
            <a class="collapse-item" href="buttons.html">Buttons</a>
            <a class="collapse-item" href="cards.html">Cards</a>
          </div>
        </div>
      </li>

      <!-- Nav Item - Utilities Collapse Menu -->
      <li class="nav-item">
        <a class="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapseUtilities" aria-expanded="true" aria-controls="collapseUtilities">
          <i class="fas fa-fw fa-wrench"></i>
          <span>Utilities</span>
        </a>
        <div id="collapseUtilities" class="collapse" aria-labelledby="headingUtilities" data-parent="#accordionSidebar">
          <div class="bg-white py-2 collapse-inner rounded">
            <h6 class="collapse-header">Custom Utilities:</h6>
            <a class="collapse-item" href="utilities-color.html">Colors</a>
            <a class="collapse-item" href="utilities-border.html">Borders</a>
            <a class="collapse-item" href="utilities-animation.html">Animations</a>
            <a class="collapse-item" href="utilities-other.html">Other</a>
          </div>
        </div>
      </li>

      <!-- Divider -->
      <hr class="sidebar-divider">

      <!-- Heading -->
      <div class="sidebar-heading">
        Addons
      </div>

      <!-- Nav Item - Pages Collapse Menu -->
      <li class="nav-item">
        <a class="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapsePages" aria-expanded="true" aria-controls="collapsePages">
          <i class="fas fa-fw fa-folder"></i>
          <span>Pages</span>
        </a>
        <div id="collapsePages" class="collapse" aria-labelledby="headingPages" data-parent="#accordionSidebar">
          <div class="bg-white py-2 collapse-inner rounded">
            <h6 class="collapse-header">Login Screens:</h6>
            <a class="collapse-item" href="login.html">Login</a>
            <a class="collapse-item" href="register.html">Register</a>
            <a class="collapse-item" href="forgot-password.html">Forgot Password</a>
            <div class="collapse-divider"></div>
            <h6 class="collapse-header">Other Pages:</h6>
            <a class="collapse-item" href="404.html">404 Page</a>
            <a class="collapse-item" href="blank.html">Blank Page</a>
          </div>
        </div>
      </li>

      <!-- Nav Item - Charts -->
      <li class="nav-item">
        <a class="nav-link" href="charts.html">
          <i class="fas fa-fw fa-chart-area"></i>
          <span>Charts</span></a>
      </li>

      <!-- Nav Item - Tables -->
      <li class="nav-item">
        <a class="nav-link" href="tables.html">
          <i class="fas fa-fw fa-table"></i>
          <span>Tables</span></a>
      </li>

      <!-- Divider -->
      <hr class="sidebar-divider d-none d-md-block">

      <!-- Sidebar Toggler (Sidebar) -->
      <div class="text-center d-none d-md-inline">
        <button class="rounded-circle border-0" id="sidebarToggle"></button>
      </div>

    </ul>
    <!-- End of Sidebar -->
"""

for nombre in archivos:
    modo = ""
    subseccion = False
    seccion = ""
    for lugar in mapa:
        if nombre in mapa[lugar]:
            subseccion = True
            seccion = lugar
    with open(nombre) as archivo:
        contenido = archivo.readlines()
    contenido_nuevo = []
    for linea in contenido:
        if not modo:
            contenido_nuevo.append(linea)
            if "<head>" in linea:
                modo = "head"
            elif "<!-- Sidebar -->" in linea:
                modo = "sidebar"
            elif "<!-- Nav Item - Dashboard -->" in linea:
                modo = "barra"
        elif modo == "head" and "</head>" in linea:
            modo = ""
            contenido_nuevo.append(head.replace("<title>Cuerpo de Tutores Ingeniería UC</title>", "<title>" + archivos[nombre] + (" | " if archivos[nombre] else "") + "Cuerpo de Tutores Ingeniería UC</title>"))
            contenido_nuevo.append(linea)
        elif modo == "sidebar" and "<!-- Sidebar - Brand -->" in linea: 
            modo = "sidebar_brand"
            contenido_nuevo.append(sidebar)
            contenido_nuevo.append(linea)
        elif modo == "sidebar_brand" and "<!-- Divider -->" in linea:
            modo = ""
            contenido_nuevo.append(sidebar_brand)
            contenido_nuevo.append(linea)
        elif modo == "barra" and "<!-- End of Sidebar -->" in linea:
            modo = ""
            lista_barra = barra.split("\n")
            for i in range(len(lista_barra)):
                if not subseccion:
                    if "nav-item" in lista_barra[i]:
                        nav_item = i
                        lista_barra[i] = lista_barra[i].replace("active", "")
                    if "nav-link" in lista_barra[i] and nombre in lista_barra[i]:
                        lista_barra[i] = lista_barra[i].replace("collapsed", "")
                        lista_barra[nav_item] = lista_barra[nav_item].replace("nav-item", "nav-item active")
                else:
                    if "nav-item" in lista_barra[i]:
                        nav_item = i
                        lista_barra[i] = lista_barra[i].replace("active", "")
                    if "class=\"collapse\"" in lista_barra[i]:
                        class_collapse = i
                    if "nav-link" in lista_barra[i]:
                        nav_link = i
                    if nombre in lista_barra[i]:
                        lista_barra[nav_item] = lista_barra[nav_item].replace("nav-item", "nav-item active")
                        lista_barra[nav_link] = lista_barra[nav_link].replace("collapsed", "")
                        lista_barra[i] = lista_barra[i].replace("collapse-item", "collapse-item active")
                        lista_barra[class_collapse] = lista_barra[class_collapse].replace("class=\"collapse\"", "class=\"collapse show\"")
            for i in lista_barra:
                contenido_nuevo.append(i)
            #contenido_nuevo.append(linea)

            
    archivo = open(nombre, "w")
    for linea in contenido_nuevo:
        archivo.write(linea + "\n")
    archivo.close()
        

        
            

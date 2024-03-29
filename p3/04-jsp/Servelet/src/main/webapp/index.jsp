<!DOCTYPE html>
<html lang="pt-br">

<head>
  <meta charset="UTF-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <!-- Web page CSS -->
  <link rel="stylesheet" href="assets/css/styles.css" />

  <!-- Simple lightbox CSS -->
  <link rel="stylesheet" href="assets/css/simple-lightbox.min.css" />

  <!-- Favicons -->
  <link rel="apple-touch-icon" sizes="180x180" href="assets/icons/apple-touch-icon.png" />
  <link rel="icon" type="image/png" sizes="32x32" href="assets/icons/favicon-32x32.png" />
  <link rel="icon" type="image/png" sizes="16x16" href="assets/icons/favicon-16x16.png" />

  <title>DALIVE Landing Page</title>
</head>

<body>
  <!-- Navbar -->
  <nav>
    <a href="#" class="logo">
      <h1>
        <span class="da">DA</span><span class="live">LIVE</span><span class="alien">&#x1f47e;</span>
      </h1>
    </a>

    <ul>
      <li class="nav-item">
        <a href="#about" class="nav-link" id="nav-link">sobre</a>
      </li>
      <li class="nav-item">
        <a href="#stars" class="nav-link" id="nav-link">estrelas</a>
      </li>
      <li class="nav-item">
        <a href="#stakeholders" class="nav-link" id="nav-link">apoiadores</a>
      </li>
      <li class="nav-item">
        <a href="#subscribe" class="nav-link" id="nav-link">assinar</a>
      </li>
    </ul>

    <div class="hamburger" id="hamburger">
      <span class="bar"></span>
      <span class="bar"></span>
      <span class="bar"></span>
    </div>

    <div class="theme-switch">
      <input type="checkbox" class="checkbox" id="checkbox">
      <label for="checkbox" class="label">
        <ion-icon name="partly-sunny-outline" class="sun"></ion-icon>
        <ion-icon name="moon-outline" class="moon"></ion-icon>
        <div class="switcher"></div>
      </label>
    </div>
  </nav>
  <!-- Dark/light theme switcher -->

  <!-- Bars -->

  <!-- Hero section -->
  <section class="hero">
    <div class="intro-text">
      <h1>
        <span class="hear">Assista nossas lives</span> <br />
        <span class="connecting">Conecte-se</span>
      </h1>
      <p>
        Uma plataforma online de streamming de games. <br />
        Com momentos especiais com games nostálgicos.
      </p>
      <a class="btn purple" href="#">saiba mais</a>
      <a class="btn grey" href="#">assinar</a>
    </div>
    <div class="i-frame">
      <iframe width="674" height="379" src="https://www.youtube.com/embed/EEQS6s7a-gk" title="alanzoka jogando RE 4 Remake | DLC Separate Ways - #1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>
  </section>
  <!-- About section -->
  <section class="about" id="about">
    <h3>Assista as transmissões</h3>
    <p>
      Transmissões 24/7, nunca fique sem diversão
    </p>

    <h3>Somente os melhores</h3>
    <p>
      Assista os melhores streamers do Brasil em um só local
    </p>
  </section>
  <!-- Lightbox image gallery -->
  <section class="stars" id="stars">
    <div class="stars-galery">
      <a href="assets/images/streamer-diana.jpg" class="big">
        <img src="assets/images/streamer-diana.jpg" alt="Diana" title="diana">
      </a>
      <a href="assets/images/streamer-alanzoka.jpeg" class="big">
        <img src="assets/images/streamer-alanzoka.jpeg" alt="Alanzoka" title="alanzoka">
      </a>
      <a href="assets/images/streamer-jovirone.jpg" class="big">
        <img src="assets/images/streamer-jovirone.jpg" alt="Jovirone" title="jovirone">
      </a>
      <a href="assets/images/streamer-casimiro.jpg" class="big">
        <img src="assets/images/streamer-casimiro.jpg" alt="Casimiro" title="casimiro">
      </a>
      <a href="assets/images/streamer-nivi.png" class="big">
        <img src="assets/images/streamer-nivi.png" alt="Nivi" title="nivi">
      </a>
      <a href="assets/images/streamer-pato.jpg" class="big">
        <img src="assets/images/streamer-pato.jpg" alt="Pato" title="pato">
      </a>
    </div>
  </section>
  <!-- Stakeholders -->
  <section class="people" id="stakeholders">
    <div class="stakeholders">
      <div class="persons">
        <div class="person-1">
          <img src="assets/images/john.jpg" alt="John Doe" />
          <p class="name">John Doe</p>
          <p class="role">Fundador</p>
        </div>
        <div class="person-2">
          <img src="assets/images/jane.jpg" alt="Jane Doe" />
          <p class="name">Jane Doe</p>
          <p class="role">Diretora de Mídia</p>
        </div>
        <div class="person-3">
          <img src="assets/images/jr.jpg" alt="John Doe Jr" />
          <p class="name">John Doe Jr</p>
          <p class="role">Assistência Técnica</p>
        </div>
      </div>
    </div>
  </section>
  <!-- Email subscription -->
  <section class="subscribe" id="subscribe">
    <h3>Assine nossa newslatter</h3>
    <form action="#">
      <input type="email" name="email" id="email-sub" class="email-sub">
      <input type="submit" value="Subscribe" class="submit-btn" id="submit-btn">
    </form>
  </section>
  <!-- Social icons -->
  <section class="social">
    <h3>Conecte-se conosco</h3>
    <div class="socicons">
      <a href="#"><ion-icon name="logo-twitter"></ion-icon></a>
      <a href="#"><ion-icon name="logo-instagram"></ion-icon></a>
      <a href="#"><ion-icon name="logo-facebook"></ion-icon></a>
    </div>
  </section>
  <footer>&copy;2023. All Rights Reserverd</footer>
  <!-- Scroll to top button -->
  <i class="scroll-up" id="scroll-up"><img src="assets/icons/upward-arrow.png" alt="up-arrow" class="socicon up-arrow"></i>
  <!-- Web page script -->
  <script src="assets/js/app.js"></script>

  <!-- Ion icons CDN -->
  <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>

  <!-- Simple lightbox -->
  <script src="assets/js/simple-lightbox.min.js"></script>
  <script>
    // Simple lightbox initializer
    let lightbox = new SimpleLightbox(".stars-galery a")
  </script>
</body>

</html>
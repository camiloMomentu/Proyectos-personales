import images from "../img/images";

const viewsInfo = [
  {
    image: {
      active: images.facturaIconLigth,
      inactive: images.facturaIconDark,
    },
    text: "Facturación",
    status: true,
    route: "/billing",
  },
  {
    image: {
      active: images.contabIconLigth,
      inactive: images.contabIconDark,
    },
    text: "Contabilidad",
    status: false,
    route: "/accounting",
  },
  {
    image: {
      active: images.gastosIconLigth,
      inactive: images.gastosIconDark,
    },
    text: "Gastos",
    status: false,
    route: "/costs",
  },
  {
    image: {
      active: images.productsLigth,
      inactive: images.productsDark,
    },
    text: "Productos",
    status: false,
    route: "/products",
  },
  {
    image: {
      active: images.ingresosLigth,
      inactive: images.ingresosDark,
    },
    text: "Ingresos",
    status: false,
    route: "/income",
  },
  {
    image: {
      active: images.changesLigth,
      inactive: images.changesDark,
    },
    text: "Cambios",
    status: false,
    route: "/changes",
  },
  {
    image: {
      active: images.clientsLigth,
      inactive: images.clientsDark,
    },
    text: "Clientes",
    status: false,
    route: "/customers",
  },
];

export default viewsInfo;

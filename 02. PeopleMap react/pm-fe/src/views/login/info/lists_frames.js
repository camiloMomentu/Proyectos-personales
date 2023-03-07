import images from "../../../images/images";

function getAxisY(nrow, row, size) {
  return (pageHeigth / nrow) * (row - 0.5) - size;
}

function getAxisX(nrow, row, size) {
  return (pageWidth / nrow) * (row - 0.5) - size;
}

const pageWidth = document.documentElement.scrollWidth;
const pageHeigth = document.documentElement.scrollHeight;

const loginFrames = [
  {
    id: 1,
    type: "",
    title: "Ingresar",
    placeholder: "",
    send_button: "",
    position: { x: getAxisX(9, 2, 90), y: getAxisY(9, 6, 40) },
    position_father: "",
    father: 0,
    image: images.login,
    input_config: {},
  },
  {
    id: 2,
    type: "input",
    title: "Correo",
    placeholder: "Email",
    send_button: "",
    position: { x: getAxisX(9, 5, 90), y: getAxisY(9, 2, 40) },
    position_father: { x: getAxisX(9, 2, 90), y: getAxisY(9, 6, 40) },
    father: 1,
    image: images.email,
    input_config: { type: "text", name: "email" },
  },
  {
    id: 3,
    type: "input",
    title: "Contraseña",
    placeholder: "Password",
    send_button: "",
    position: { x: getAxisX(9, 6, 90), y: getAxisY(9, 4, 40) },
    position_father: { x: getAxisX(9, 2, 90), y: getAxisY(9, 6, 40) },
    father: 1,
    image: images.password,
    input_config: { type: "password", name: "password" },
  },
  {
    id: 4,
    type: "",
    title: "Registrarse",
    placeholder: "",
    send_button: "",
    position: { x: getAxisX(9, 8, 90), y: getAxisY(9, 6, 40) },
    position_father: { x: getAxisX(9, 2, 90), y: getAxisY(9, 6, 40) },
    father: 1,
    image: images.register,
    input_config: {},
  },
  {
    id: 5,
    type: "input",
    title: "Recuperar contraseña",
    placeholder: "Email",
    send_button: true,
    position: { x: getAxisX(9, 7, 90), y: getAxisY(9, 8, 40) },
    position_father: { x: getAxisX(9, 2, 90), y: getAxisY(9, 6, 40) },
    father: 1,
    image: images.forguet,
    input_config: { type: "text", name: "forguet" },
  },
];

export default loginFrames;

const petitions = {
  host: "http://127.0.0.1",
  port: 8080,
  config: {
    headers: {
      Authorization: "Bearer " + "123",
    },
  },
};

const adminOptions = [
  { title: "Empleados", path: "/employees" },
  { title: "Vacaciones", path: "/vacations" },
  { title: "Ausentismo", path: "/absenteeism" },
  { title: "Retiros", path: "/retirement" },
  { title: "Pensiones", path: "/pensions" },
  { title: "Cargos", path: "/positions" },
];

export { petitions, adminOptions };

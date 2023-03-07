import React, { useState } from "react";
import "./index.css";
import { UserSVG } from "../../components/svg/SVGs";
import images from "../../images/images";
import MenuAdmin from "../../components/menus/menuAdmin/menuAdmin";
import PeopleMap from "../../views/map/index";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { adminOptions } from "../../config";
import Employees from "./components/employees";
import Vacations from "./components/vacations";
import Absenteeism from "./components/absenteeism";
import Retirement from "./components/retirement";
import Pensions from "./components/pensions";
import Positions from "./components/positions";

export default function Data({ handleExit }) {
  const [activePM, setActivePM] = useState(false);

  function exit() {
    handleExit(false);
    window.location.reload(true);
  }

  function handlePM() {
    if (activePM) {
      setActivePM(false);
    } else {
      setActivePM(true);
    }
  }

  return (
    <>
      {activePM ? (
        <PeopleMap handleAdmin={handlePM} />
      ) : (
        <Router>
          <div className="data_container">
            <header className="header_data">
              <div className="logo_container">
                <img src={images.logo} />
                <p>Portal de administración</p>
              </div>

              <div className="user_container">
                <button onClick={exit}>
                  <UserSVG />
                </button>
              </div>
            </header>

            <div className="content_admin_container">
              <MenuAdmin options={adminOptions} handlePM={handlePM} />
              <div className="RoutesContainer">
                <Routes>
                  <Route path={"/employees"} element={<Employees />} />
                  <Route path={"/vacations"} element={<Vacations />} />
                  <Route path={"/absenteeism"} element={<Absenteeism />} />
                  <Route path={"/retirement"} element={<Retirement />} />
                  <Route path={"/pensions"} element={<Pensions />} />
                  <Route path={"/positions"} element={<Positions />} />
                  <Route path={"/"} element={<Employees />} />
                </Routes>
              </div>
            </div>
          </div>
        </Router>
      )}
    </>
  );
}

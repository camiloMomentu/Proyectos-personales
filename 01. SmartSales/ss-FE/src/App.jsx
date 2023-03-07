import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import MenuHome from "./components/home/index";
import viewsInfo from "./info/views";
import titles from "./info/titles";
import Billing from "./views/billing/billing";
import Accounting from "./views/accounting/accounting";
import Changes from "./views/changes/changes";
import Costs from "./views/costs/costs";
import Customers from "./views/customers/customers";
import Income from "./views/income/income";
import Products from "./views/products/products";
import Home from "./views/home/home";

export default function App() {
  return (
    <>
      <Router>
        <MenuHome title={titles["/"]} buttons={viewsInfo} />
        <Routes>
          <Route path={"/customers"} element={<Customers />} />
          <Route path={"/changes"} element={<Changes />} />
          <Route path={"/income"} element={<Income />} />
          <Route path={"/products"} element={<Products />} />
          <Route path={"/costs"} element={<Costs />} />
          <Route path={"/accounting"} element={<Accounting />} />
          <Route path={"/billing"} element={<Billing />} />
          <Route path={"/"} element={<Home />} />
        </Routes>
      </Router>
    </>
  );
}

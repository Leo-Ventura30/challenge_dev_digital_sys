import { useState } from "react";
import ProposalContainer from "../containers";
import api from "../../../services/api";

let options = {
  method: "POST",
  url: "/customers/",
  headers: {
    cookie: "csrftoken=KHUnYC6UU6sc4MaqMiKpTRSSmKN6VSK2",
    "Content-Type": "application/json",
  },
  data: {
    full_name: "Leo",
    cpf_cnpj: "565656",
    address: "dasdsada asdsdas",
    value: 15000,
  },
};

const ProposalScreen = () => {
  const [data, setData] = useState("");
  const [customer, setCustomer] = useState("");

  const onChange = (e, name) => {
    setData((prev) => ({ ...prev, [name]: e }));
  };

  const createProposal = async () => {
    console.log(data);
    const res = await api.post("/customers/", data);
    setCustomer(res.data);
  };

  return (
    <ProposalContainer
      data={data}
      customerData={customer}
      onChange={onChange}
      onSubmit={createProposal}
    />
  );
};

export default ProposalScreen;

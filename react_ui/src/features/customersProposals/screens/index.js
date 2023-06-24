import { useState } from "react";
import ProposalContainer from "../containers";
import api from "../../../services/api";

const ProposalScreen = () => {
  const [data, setData] = useState("");
  const [customer, setCustomer] = useState("");

  const onChange = (e, name) => {
    setData((prev) => ({ ...prev, [name]: e }));
  };

  const createProposal = async () => {
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

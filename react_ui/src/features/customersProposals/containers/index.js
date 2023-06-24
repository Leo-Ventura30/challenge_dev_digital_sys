import { DefaultButton, HeaderProposals } from "../../../components";

const ProposalContainer = ({ data, customerData, onChange, onSubmit }) => (
  <div className="App-container">
    <div>
      <HeaderProposals />
    </div>
    <form style={{ flex: 1, display: "flex", flexDirection: "column" }}>
      <DefaultButton
        id="full_name"
        name={"Nome completo"}
        placeholder={"Insira seu nome completo."}
        onChange={(e) => onChange(e.target.value, e.target.id)}
        value={data.name}
      />
      <DefaultButton
        id="cpf_cnpj"
        name={"CPF ou CNPJ"}
        placeholder={"CPF ou CNPJ valido."}
        onChange={(e) => onChange(e.target.value, e.target.id)}
        type={"number"}
        value={data.cpfcnpj}
      />
      <DefaultButton
        id="address"
        name={"Endereço"}
        placeholder={"Preencha o endereço completo."}
        onChange={(e) => onChange(e.target.value, e.target.id)}
        value={data.address}
      />
      <DefaultButton
        id="value"
        name={"Valor"}
        placeholder={"Valor do empréstimos."}
        onChange={(e) => onChange(e.target.value, e.target.id)}
        value={data.value}
        type={"number"}
      />
      <button style={{ width: "100%", padding: 6 }} onSubmit={() => onSubmit()}>
        Enviar proposta
      </button>
    </form>

    {customerData && (
      <div
        style={{
          margin: 6,
          display: "flex",
          flexDirection: "column",
          alignItems: "flex-start",
          background: "#bbb",
          color: "#d24",
          fontSize: 18,
          padding: 6,
          width: "320px",
        }}
      >
        <p>Nome completo</p>
        <div>{customerData.full_name}</div>
        <p>CPF/CNPJ</p>
        <div>{customerData.cpf_cnpj}</div>
        <p>Score</p>
        <div>{customerData.score}</div>
        <p>Endereço</p>
        <div>{customerData.address}</div>
        <p>Valor solicitado</p>
        <div>{customerData.value}</div>
        <p>Status da proposta</p>
        <div>{customerData.status}</div>
        <p>Data de criação</p>
        <div>{customerData.created_at}</div>
      </div>
    )}
  </div>
);

export default ProposalContainer;

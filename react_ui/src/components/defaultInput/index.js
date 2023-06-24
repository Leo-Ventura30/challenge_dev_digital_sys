const DefaultButton = (props, { name }) => (
  <input
    style={{
      padding: 6,
      fontSize: 16,
      marginBottom: 4,
      width: "320px",
      border: 0,
    }}
    // required
    {...props}
  />
);

export default DefaultButton;

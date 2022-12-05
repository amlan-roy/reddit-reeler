import "./App.css";
import TopButtons from "./components/TopButtons";
import Container from "@mui/material/Container";
import ImagesList from "./components/ImagesList";

function App() {
  return (
    <div className="App flex" style={{ backgroundColor: "#cfe8fc" }}>
      <Container maxWidth="md" sx={{ bgcolor: "white", height: "100vh" }}>
        <h1 className="font-sans text-4xl font-black">Reddit Reeler</h1>
        <TopButtons />
        <ImagesList />
      </Container>
    </div>
  );
}

export default App;

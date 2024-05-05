import "./style/app.css";
import "./style/reset.css";
import App from "./App.svelte";

const app = new App({
	target: document.getElementById("app"),
});

export default app;

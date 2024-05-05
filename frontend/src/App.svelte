<script lang="ts">
	import Chat from "./components/Chat.svelte";
	import ThemeToggle from "./components/ThemeToggle.svelte";
</script>

<main class="flex-col">
	<ThemeToggle />
	<Chat />
</main>

<style>
	main {
		width: 100%;
		height: 100vh;
		justify-content: center;
		padding: 1.25% 31.25%;
	}

	@media only screen and (min-width: 769px) and (max-width: 1024px) {
		main {
			padding: 1.2% 25%;
		}
	}

	@media only screen and (max-width: 768px) {
		main {
			padding: 0;
		}
	}
</style>

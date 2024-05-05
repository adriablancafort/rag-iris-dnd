<script lang="ts">
	import { IconMoonFilled, IconSunFilled } from "@tabler/icons-svelte";
	import { onMount } from "svelte";

	let theme: string = localStorage.getItem("theme") as string;
	if (!theme) theme = "dark";

	let size: number = 24;

	function changeTheme() {
		theme = theme !== "dark" ? "dark" : "light";
		localStorage.setItem("theme", theme);
		setTheme();
	}

	function setTheme() {
		document.documentElement.style.colorScheme = theme;
		document.body.className = theme;
	}

	onMount(() => {
		setTheme();
	});
</script>

<button
	class="theme-toggle flex-col"
	type="button"
	aria-label="Theme toggle"
	tabindex="0"
	on:click={changeTheme}
>
	{#if theme !== "dark"}
		<IconSunFilled {size} aria-hidden="true" />
	{:else}
		<IconMoonFilled {size} aria-hidden="true" />
	{/if}
</button>

<style>
	.theme-toggle {
		position: absolute;
		top: 0.5rem;
		right: 0.5rem;
		padding: 0.5rem;
		border-radius: 0.5rem;
	}

	.theme-toggle:hover {
		cursor: pointer;
	}
</style>

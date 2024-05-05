<script lang="ts">
	import { afterUpdate } from "svelte";

	let logContainer: HTMLElement;

	afterUpdate(() => {
		logContainer.scrollTop = logContainer.scrollHeight;
	});
</script>

<section
	class="message-log flex-col"
	aria-label="Message log"
	bind:this={logContainer}
>
	<slot />
</section>

<style>
	.message-log {
		height: 90%;
		width: 100%;
		padding: 0 1rem 0 0;
		overflow-y: auto;
		row-gap: 1rem;
	}
</style>

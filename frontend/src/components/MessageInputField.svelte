<div class="message-input-container flex-col">
	<div
		class="message-input-field textarea-like text-wrap theme-secondary"
		contenteditable="true"
		role="textbox"
		aria-label="Message input field"
		tabindex="0"
		on:keydown
	/>
</div>

<style>
	.message-input-container {
		height: 10%;
		width: 100%;
		justify-content: flex-end;
	}

	.message-input-field {
		width: 100%;
		padding: 1rem;
		border-radius: 0.25rem;
	}

	@media only screen and (max-width: 768px) {
		.message-input-field {
			padding: 0.5rem;
		}
	}
</style>

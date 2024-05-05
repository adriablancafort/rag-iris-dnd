<script lang="ts">
import MessageLog from "./MessageLog.svelte";
import MessageLogEntry from "./MessageLogEntry.svelte";

let messages = [["bot", "Introduce any Url and ask me about its content!"]];

async function sendMessage(event) {
    let msg = '';

    if (event instanceof KeyboardEvent && event.keyCode === 13) {
	event.preventDefault();
	msg = (event.target as HTMLElement).innerText.trim();
	(event.target as HTMLElement).innerText = "";
    } else {
	msg = document.querySelector('.message-input-field').innerText.trim();
	document.querySelector('.message-input-field').innerText = "";
    }

    if (!msg || msg === "") return;

    messages = [...messages, ["user", msg]];

    isLoading1 = true;

    try {
	const response = await fetch(`http://127.0.0.1:8000/ask/${encodeURIComponent(msg)}`)
	    .then(res => res.json())
	    .then(data => data.response);

	messages = [...messages, ["bot", response]];
    } catch (error) {
	messages = [...messages, ["bot", error.message]];
    } finally  {
	isLoading1 = false;
    }
}

let url = '';

let isLoading1 = false;
let isLoading2 = false;

async function sendUrl(event) {
    if (event instanceof KeyboardEvent && event.keyCode === 13) {
        event.preventDefault();
    }

    isLoading2 = true;

    try {
        await fetch(`http://127.0.0.1:8000/get_url/${encodeURIComponent(url)}`);
    } catch (error) {
        // Handle error
    } finally {
        isLoading2 = false;
    }
}
</script>

<h1 class="heading-title">Retrieval Agumented Generation Assistent</h1>

<article class="chat flex-col theme-primary" aria-label="Chat">
	<MessageLog>
		{#each messages as [sender, message]}
			<MessageLogEntry {sender} {message} />
		{/each}
	</MessageLog>
	<div class="message-input-container flex-col">
	    <div
		class="message-input-field textarea-like text-wrap theme-secondary"
		contenteditable="true"
		role="textbox"
		aria-label="Message input field"
		tabindex="0"
		on:keydown={(event) => { if (event.keyCode === 13) sendMessage(event); }}
	    />
	    <button class="send-button" on:click={sendMessage}>
	    {#if isLoading1}
		<img src="/loading.svg" alt="Loading..." class="loading-spiner" />
	    {:else}
		Send
	    {/if}
	    </button>
	</div>
	<div class="message-input-container flex-col">
		<input
			class="message-input-field textarea-like text-wrap theme-secondary"
			type="url"
			aria-label="Message input field"
			tabindex="0"
			placeholder="Website Url"
			bind:value={url}
			on:keydown={(event) => { if (event.keyCode === 13) sendUrl(event); }}
		/>
		<button class="send-button" on:click={sendUrl}>
			{#if isLoading2}
				<img src="/loading.svg" alt="Loading..." class="loading-spiner" />
			{:else}
				Send
			{/if}
		</button>
	</div>
</article>

<style>
	.heading-title {
		text-align: center;
		font-size: 3rem;
		line-height: 3.8rem;
		font-weight: 700;
		margin: 1.5rem 0;
	}
	
	.chat {
		width: 100%;
		height: 85%;
		padding: 1rem;
		align-items: center;
		border-radius: 1rem;
		box-shadow: 0 0 7rem rgba(180, 180, 180, 0.5);
	}
	
	.message-input-container {
		height: 15%;
		width: 100%;
		justify-content: flex-end; position: relative;
	}
	
	.message-input-field {
		width: 100%;
		padding: 1rem;
		padding-right: 4rem;
		border-radius: 0.5rem;
		font-size: 16px;
	}

	.send-button {
		position: absolute;
		right: 0.5rem;
		bottom: 0.5rem;
		padding: 0.5rem;
		background-color: var(--bg-color-accent);
		border-radius: 0.2rem;
	}
	
	.loading-spiner {
		animation: spin 1s infinite linear;
	}
	
	@keyframes spin {
		from {
			transform: rotate(0deg);
		}
		to {
			transform: rotate(360deg);
		}
	}

	@media only screen and (max-width: 768px) {
		.message-input-field {
		    padding: 0.5rem;
		}
	}
</style>

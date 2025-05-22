<script>
  let messages = [];
  let text = '';
  async function send() {
    if (!text) return;
    messages = [...messages, { from: 'me', text }];
    const res = await fetch('/register', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ this: text, who: 'user', did: 'said', when: new Date().toISOString(), confirmed_by: '', if_ok: '', if_doubt: '', if_not: '', status: 'pending' })
    });
    const data = await res.json();
    messages = [...messages, { from: 'server', text: data.status }];
    text = '';
  }
</script>

<main>
  <div class="history">
    {#each messages as msg}
      <div class={msg.from}>{msg.text}</div>
    {/each}
  </div>
  <input bind:value={text} placeholder="mensagem" on:keydown={(e)=>e.key==='Enter' && send()} />
  <button on:click={send}>Enviar</button>
</main>

<style>
  main { display: flex; flex-direction: column; gap: 0.5rem; max-width: 400px; margin: auto; }
  .history { min-height: 200px; border: 1px solid #ccc; padding: 0.5rem; overflow-y: auto; }
  .me { text-align: right; }
  input, button { font-size: 1rem; }
</style>

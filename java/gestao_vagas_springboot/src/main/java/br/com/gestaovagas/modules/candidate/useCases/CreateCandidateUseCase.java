package br.com.gestaovagas.modules.candidate.useCases;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import br.com.gestaovagas.exceptions.UserAlreadyExists;
import br.com.gestaovagas.modules.candidate.CandidateEntity;
import br.com.gestaovagas.modules.candidate.CandidateRepository;

@Service
public class CreateCandidateUseCase {
    @Autowired
    private CandidateRepository candidateRepository;

    public CandidateEntity execute(CandidateEntity candidateEntity) {
        this.candidateRepository
                .findByUsernameOrEmail(candidateEntity.getUsername(), candidateEntity.getEmail())
                .ifPresent((user) -> {
                    throw new UserAlreadyExists();
                });

        return this.candidateRepository.save(candidateEntity);
    }
}
